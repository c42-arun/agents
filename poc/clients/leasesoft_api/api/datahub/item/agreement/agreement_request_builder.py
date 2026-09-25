from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .....models.ls_agreement import LsAgreement
    from .assets.assets_request_builder import AssetsRequestBuilder
    from .documents.documents_request_builder import DocumentsRequestBuilder
    from .has_vehicle_asset.has_vehicle_asset_request_builder import HasVehicleAssetRequestBuilder

class AgreementRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/datahub/{goldenRecordId}/agreement
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AgreementRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/datahub/{goldenRecordId}/agreement{?agreementNo*,noCache*,tenantSchema*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[AgreementRequestBuilderGetQueryParameters]] = None) -> Optional[LsAgreement]:
        """
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LsAgreement]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.ls_agreement import LsAgreement

        return await self.request_adapter.send_async(request_info, LsAgreement, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[AgreementRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def with_url(self,raw_url: str) -> AgreementRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AgreementRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AgreementRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def assets(self) -> AssetsRequestBuilder:
        """
        The assets property
        """
        from .assets.assets_request_builder import AssetsRequestBuilder

        return AssetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def documents(self) -> DocumentsRequestBuilder:
        """
        The documents property
        """
        from .documents.documents_request_builder import DocumentsRequestBuilder

        return DocumentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def has_vehicle_asset(self) -> HasVehicleAssetRequestBuilder:
        """
        The hasVehicleAsset property
        """
        from .has_vehicle_asset.has_vehicle_asset_request_builder import HasVehicleAssetRequestBuilder

        return HasVehicleAssetRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AgreementRequestBuilderGetQueryParameters():
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "agreement_no":
                return "agreementNo"
            if original_name == "no_cache":
                return "noCache"
            if original_name == "tenant_schema":
                return "tenantSchema"
            return original_name
        
        agreement_no: Optional[str] = None

        no_cache: Optional[bool] = None

        tenant_schema: Optional[str] = None

    
    @dataclass
    class AgreementRequestBuilderGetRequestConfiguration(RequestConfiguration[AgreementRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

