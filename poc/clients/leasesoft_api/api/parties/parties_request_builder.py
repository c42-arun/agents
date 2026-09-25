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
    from ...models.ls_party import LsParty
    from .item.with_short_code_name_item_request_builder import WithShortCodeNameItemRequestBuilder

class PartiesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/parties
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PartiesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/parties{?agreementNo*,includeContacts*,tenantSchema*}", path_parameters)
    
    def by_short_code_name(self,short_code_name: str) -> WithShortCodeNameItemRequestBuilder:
        """
        Gets an item from the clients.leasesoft_api.api.parties.item collection
        param short_code_name: Unique identifier of the item
        Returns: WithShortCodeNameItemRequestBuilder
        """
        if short_code_name is None:
            raise TypeError("short_code_name cannot be null.")
        from .item.with_short_code_name_item_request_builder import WithShortCodeNameItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["shortCodeName"] = short_code_name
        return WithShortCodeNameItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PartiesRequestBuilderGetQueryParameters]] = None) -> Optional[list[LsParty]]:
        """
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[LsParty]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.ls_party import LsParty

        return await self.request_adapter.send_collection_async(request_info, LsParty, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PartiesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "text/plain;q=0.9")
        return request_info
    
    def with_url(self,raw_url: str) -> PartiesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PartiesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PartiesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PartiesRequestBuilderGetQueryParameters():
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
            if original_name == "include_contacts":
                return "includeContacts"
            if original_name == "tenant_schema":
                return "tenantSchema"
            return original_name
        
        agreement_no: Optional[str] = None

        include_contacts: Optional[bool] = None

        tenant_schema: Optional[str] = None

    
    @dataclass
    class PartiesRequestBuilderGetRequestConfiguration(RequestConfiguration[PartiesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

