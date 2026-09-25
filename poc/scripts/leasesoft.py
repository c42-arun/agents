from __future__ import annotations

import os
import ssl
from pathlib import Path
from urllib.parse import urlparse

import httpx
import truststore
from azure.identity.aio import ClientSecretCredential
from dotenv import load_dotenv
from kiota_authentication_azure.azure_identity_authentication_provider import (
    AzureIdentityAuthenticationProvider,
)
from kiota_http.httpx_request_adapter import HttpxRequestAdapter
from kiota_http.kiota_client_factory import KiotaClientFactory

from clients.leasesoft_api.leasesoft_api_client import LeasesoftApiClient


TENANT_ID = "6d6a11bc-469a-48df-a548-d3f353ac1be8"
DEFAULT_SCOPE = "api://aadapp-leasesoft-api-nonprod.investec.io/.default"


class ConfiguredLeasesoftApiClient(LeasesoftApiClient):
    def __init__(
        self,
        request_adapter: HttpxRequestAdapter,
        credential: ClientSecretCredential,
        http_client: httpx.AsyncClient,
    ) -> None:
        super().__init__(request_adapter)
        self._credential = credential
        self._http_client = http_client

    async def close(self) -> None:
        await self._http_client.aclose()
        await self._credential.close()

    async def __aenter__(self) -> ConfiguredLeasesoftApiClient:
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.close()


def create_leasesoft_client(
    env_path: str | Path | None = None,
) -> ConfiguredLeasesoftApiClient:
    path = Path(env_path) if env_path else Path(__file__).resolve().parents[1] / ".env"
    load_dotenv(path)

    def required(name: str) -> str:
        value = os.getenv(name, "").strip()
        if not value:
            raise ValueError(f"Missing required environment variable: {name}")
        return value

    base_url = required("LEASESOFT_API_BASE_URL").rstrip("/")
    hostname = urlparse(base_url).hostname
    if not hostname:
        raise ValueError("LEASESOFT_API_BASE_URL must be a valid URL")

    truststore.inject_into_ssl()
    credential = ClientSecretCredential(
        tenant_id=TENANT_ID,
        client_id=required("LEASESOFT_CLIENT_ID"),
        client_secret=required("LEASESOFT_CLIENT_SECRET"),
    )
    auth_provider = AzureIdentityAuthenticationProvider(
        credential,
        scopes=[os.getenv("LEASESOFT_SCOPE", DEFAULT_SCOPE).strip() or DEFAULT_SCOPE],
        allowed_hosts=[hostname],
    )

    native_client = httpx.AsyncClient(
        verify=truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT),
        timeout=30,
    )
    http_client = KiotaClientFactory.create_with_default_middleware(native_client)
    request_adapter = HttpxRequestAdapter(auth_provider, http_client=http_client)
    request_adapter.base_url = base_url

    return ConfiguredLeasesoftApiClient(
        request_adapter,
        credential,
        http_client,
    )