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
    from .......models.ls_settlement_upgrade_quote import LsSettlementUpgradeQuote
    from .individual_schema.individual_schema_request_builder import IndividualSchemaRequestBuilder

class SettlementUpgradeQuotesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/schemas/{tenantSchema}/agreements/{agreementNo}/settlement-upgrade-quotes
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SettlementUpgradeQuotesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/schemas/{tenantSchema}/agreements/{agreementNo}/settlement-upgrade-quotes{?goldenRecordId*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SettlementUpgradeQuotesRequestBuilderGetQueryParameters]] = None) -> Optional[list[LsSettlementUpgradeQuote]]:
        """
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[LsSettlementUpgradeQuote]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.ls_settlement_upgrade_quote import LsSettlementUpgradeQuote

        return await self.request_adapter.send_collection_async(request_info, LsSettlementUpgradeQuote, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SettlementUpgradeQuotesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "text/plain;q=0.9")
        return request_info
    
    def with_url(self,raw_url: str) -> SettlementUpgradeQuotesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SettlementUpgradeQuotesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SettlementUpgradeQuotesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def individual_schema(self) -> IndividualSchemaRequestBuilder:
        """
        The individualSchema property
        """
        from .individual_schema.individual_schema_request_builder import IndividualSchemaRequestBuilder

        return IndividualSchemaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SettlementUpgradeQuotesRequestBuilderGetQueryParameters():
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "golden_record_id":
                return "goldenRecordId"
            return original_name
        
        golden_record_id: Optional[str] = None

    
    @dataclass
    class SettlementUpgradeQuotesRequestBuilderGetRequestConfiguration(RequestConfiguration[SettlementUpgradeQuotesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

