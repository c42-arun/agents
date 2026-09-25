from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_shortname_item_request_builder import WithShortnameItemRequestBuilder

class WithSchemaItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/datahub/query/{schema}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithSchemaItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/datahub/query/{schema}", path_parameters)
    
    def by_shortname(self,shortname: str) -> WithShortnameItemRequestBuilder:
        """
        Gets an item from the clients.leasesoft_api.api.datahub.query.item.item collection
        param shortname: Unique identifier of the item
        Returns: WithShortnameItemRequestBuilder
        """
        if shortname is None:
            raise TypeError("shortname cannot be null.")
        from .item.with_shortname_item_request_builder import WithShortnameItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["shortname"] = shortname
        return WithShortnameItemRequestBuilder(self.request_adapter, url_tpl_params)
    

