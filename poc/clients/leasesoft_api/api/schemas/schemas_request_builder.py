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
    from ...models.ls_problem_details import LsProblemDetails
    from .item.with_tenant_schema_item_request_builder import WithTenantSchemaItemRequestBuilder

class SchemasRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/schemas
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SchemasRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/schemas", path_parameters)
    
    def by_tenant_schema(self,tenant_schema: str) -> WithTenantSchemaItemRequestBuilder:
        """
        Gets an item from the clients.leasesoft_api.api.schemas.item collection
        param tenant_schema: Unique identifier of the item
        Returns: WithTenantSchemaItemRequestBuilder
        """
        if tenant_schema is None:
            raise TypeError("tenant_schema cannot be null.")
        from .item.with_tenant_schema_item_request_builder import WithTenantSchemaItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["tenantSchema"] = tenant_schema
        return WithTenantSchemaItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SchemasRequestBuilderGetQueryParameters]] = None) -> Optional[list[str]]:
        """
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[str]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.ls_problem_details import LsProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "404": LsProblemDetails,
            "XXX": LsProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_collection_of_primitive_async(request_info, str, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SchemasRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "text/plain;q=0.9")
        return request_info
    
    def with_url(self,raw_url: str) -> SchemasRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SchemasRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SchemasRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class SchemasRequestBuilderGetQueryParameters():
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "data_hub_id":
                return "dataHubId"
            return original_name
        
        data_hub_id: Optional[str] = None

    
    @dataclass
    class SchemasRequestBuilderGetRequestConfiguration(RequestConfiguration[SchemasRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

