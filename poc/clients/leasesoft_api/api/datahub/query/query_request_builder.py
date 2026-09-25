from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_schema_item_request_builder import WithSchemaItemRequestBuilder

class QueryRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/datahub/query
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new QueryRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/datahub/query", path_parameters)
    
    def by_schema(self,schema: str) -> WithSchemaItemRequestBuilder:
        """
        Gets an item from the clients.leasesoft_api.api.datahub.query.item collection
        param schema: Unique identifier of the item
        Returns: WithSchemaItemRequestBuilder
        """
        if schema is None:
            raise TypeError("schema cannot be null.")
        from .item.with_schema_item_request_builder import WithSchemaItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["schema"] = schema
        return WithSchemaItemRequestBuilder(self.request_adapter, url_tpl_params)
    

