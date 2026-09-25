from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .branch.branch_request_builder import BranchRequestBuilder
    from .item.with_edi_message_item_request_builder import WithEdiMessageItemRequestBuilder
    from .operator.operator_request_builder import OperatorRequestBuilder

class EdiMessageRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/Schemas/{tenantSchema}/edi-message
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EdiMessageRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/Schemas/{tenantSchema}/edi-message", path_parameters)
    
    def by_edi_message_id(self,edi_message_id: str) -> WithEdiMessageItemRequestBuilder:
        """
        Gets an item from the clients.leasesoft_api.api.Schemas.item.ediMessage.item collection
        param edi_message_id: Unique identifier of the item
        Returns: WithEdiMessageItemRequestBuilder
        """
        if edi_message_id is None:
            raise TypeError("edi_message_id cannot be null.")
        from .item.with_edi_message_item_request_builder import WithEdiMessageItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ediMessageId"] = edi_message_id
        return WithEdiMessageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def branch(self) -> BranchRequestBuilder:
        """
        The branch property
        """
        from .branch.branch_request_builder import BranchRequestBuilder

        return BranchRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operator(self) -> OperatorRequestBuilder:
        """
        The operator property
        """
        from .operator.operator_request_builder import OperatorRequestBuilder

        return OperatorRequestBuilder(self.request_adapter, self.path_parameters)
    

