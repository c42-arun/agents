from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_document_type_item_request_builder import WithDocumentTypeItemRequestBuilder

class ByTypeRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/documents/by-type
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ByTypeRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/documents/by-type", path_parameters)
    
    def by_document_type(self,document_type: str) -> WithDocumentTypeItemRequestBuilder:
        """
        Gets an item from the clients.leasesoft_api.api.documents.byType.item collection
        param document_type: Unique identifier of the item
        Returns: WithDocumentTypeItemRequestBuilder
        """
        if document_type is None:
            raise TypeError("document_type cannot be null.")
        from .item.with_document_type_item_request_builder import WithDocumentTypeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["documentType"] = document_type
        return WithDocumentTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    

