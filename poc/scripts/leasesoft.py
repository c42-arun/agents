from __future__ import annotations

import os
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import quote

import truststore

truststore.inject_into_ssl()

import requests
from dotenv import load_dotenv


DEFAULT_TOKEN_URL = (
    "https://login.microsoftonline.com/6d6a11bc-469a-48df-a548-d3f353ac1be8/"
    "oauth2/v2.0/token"
)
DEFAULT_SCOPE = "api://aadapp-leasesoft-api-nonprod.investec.io/.default"


@dataclass(frozen=True)
class LeaseSoftConfig:
    api_base_url: str
    client_id: str
    client_secret: str = field(repr=False)
    token_url: str = DEFAULT_TOKEN_URL
    scope: str = DEFAULT_SCOPE
    timeout_seconds: float = 30.0

    @classmethod
    def from_env(cls, env_path: str | Path | None = None) -> LeaseSoftConfig:
        path = Path(env_path) if env_path else Path(__file__).resolve().parents[1] / ".env"
        load_dotenv(path)

        def required(name: str) -> str:
            value = os.getenv(name, "").strip()
            if not value:
                raise ValueError(f"Missing required environment variable: {name}")
            return value

        return cls(
            api_base_url=required("LEASESOFT_API_BASE_URL").rstrip("/"),
            client_id=required("LEASESOFT_CLIENT_ID"),
            client_secret=required("LEASESOFT_CLIENT_SECRET"),
            token_url=os.getenv("LEASESOFT_TOKEN_URL", DEFAULT_TOKEN_URL).strip(),
            scope=os.getenv("LEASESOFT_SCOPE", DEFAULT_SCOPE).strip(),
        )


class LeaseSoftClient:
    def __init__(
        self,
        config: LeaseSoftConfig,
        session: requests.Session | None = None,
    ) -> None:
        self.config = config
        self.session = session or requests.Session()
        self._access_token: str | None = None
        self._token_expires_at = 0.0

    @classmethod
    def from_env(cls, env_path: str | Path | None = None) -> LeaseSoftClient:
        return cls(LeaseSoftConfig.from_env(env_path))

    def _get_access_token(self) -> str:
        if self._access_token and time.monotonic() < self._token_expires_at:
            return self._access_token

        response = self.session.post(
            self.config.token_url,
            data={
                "grant_type": "client_credentials",
                "client_id": self.config.client_id,
                "client_secret": self.config.client_secret,
                "scope": self.config.scope,
            },
            timeout=self.config.timeout_seconds,
        )
        response.raise_for_status()
        payload = response.json()

        access_token = payload.get("access_token")
        if not isinstance(access_token, str) or not access_token:
            raise ValueError("OAuth response did not contain an access_token")

        expires_in = float(payload.get("expires_in", 3600))
        self._access_token = access_token
        self._token_expires_at = time.monotonic() + max(0, expires_in - 60)
        return access_token

    def get_agreement(
        self,
        agreement_no: str,
        *,
        tenant_schema: str | None = None,
        include_historical: bool = False,
        include_bank_details: bool = False,
        no_cache: bool = False,
    ) -> dict[str, Any]:
        if not agreement_no.strip():
            raise ValueError("agreement_no must not be empty")

        params: dict[str, str | bool] = {
            "noCache": no_cache,
            "includeHistorical": include_historical,
            "includeBankDetails": include_bank_details,
        }
        if tenant_schema:
            params["tenantSchema"] = tenant_schema

        response = self.session.get(
            f"{self.config.api_base_url}/api/agreements/{agreement_no}",
            headers={
                "Authorization": f"Bearer {self._get_access_token()}",
                "Accept": "application/json",
            },
            params=params,
            timeout=self.config.timeout_seconds,
        )
        response.raise_for_status()
        payload = response.json()
        if not isinstance(payload, dict):
            raise ValueError("Agreement response was not a JSON object")
        return payload

    def get_titles(self, tenant_schema: str) -> list[dict[str, Any]]:
        if not tenant_schema.strip():
            raise ValueError("tenant_schema must not be empty")

        encoded_schema = quote(tenant_schema, safe="")
        response = self.session.get(
            f"{self.config.api_base_url}/api/Schemas/{encoded_schema}/titles",
            headers={
                "Authorization": f"Bearer {self._get_access_token()}",
                "Accept": "application/json",
            },
            timeout=self.config.timeout_seconds,
        )
        response.raise_for_status()
        payload = response.json()
        if not isinstance(payload, list) or not all(
            isinstance(title, dict) for title in payload
        ):
            raise ValueError("Titles response was not a JSON array of objects")
        return payload