from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.proposal_no_item_request_builder import ProposalNoItemRequestBuilder

class ProposalsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/Proposals
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ProposalsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/Proposals", path_parameters)
    
    def by_proposal_no_id(self,proposal_no_id: str) -> ProposalNoItemRequestBuilder:
        """
        Gets an item from the clients.leasesoft_api.api.Proposals.item collection
        param proposal_no_id: Unique identifier of the item
        Returns: ProposalNoItemRequestBuilder
        """
        if proposal_no_id is None:
            raise TypeError("proposal_no_id cannot be null.")
        from .item.proposal_no_item_request_builder import ProposalNoItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["proposalNo%2Did"] = proposal_no_id
        return ProposalNoItemRequestBuilder(self.request_adapter, url_tpl_params)
    

