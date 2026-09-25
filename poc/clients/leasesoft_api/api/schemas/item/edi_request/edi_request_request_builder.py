from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_edi_request_item_request_builder import WithEdiRequestItemRequestBuilder

class EdiRequestRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/Schemas/{tenantSchema}/edi-request
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EdiRequestRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/Schemas/{tenantSchema}/edi-request", path_parameters)
    
    def by_edi_request_id(self,edi_request_id: str) -> WithEdiRequestItemRequestBuilder:
        """
        Gets an item from the clients.leasesoft_api.api.Schemas.item.ediRequest.item collection
        param edi_request_id: Unique identifier of the item
        Returns: WithEdiRequestItemRequestBuilder
        """
        if edi_request_id is None:
            raise TypeError("edi_request_id cannot be null.")
        from .item.with_edi_request_item_request_builder import WithEdiRequestItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ediRequestId"] = edi_request_id
        return WithEdiRequestItemRequestBuilder(self.request_adapter, url_tpl_params)
    

