from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_agreement_no_item_request_builder import WithAgreementNoItemRequestBuilder

class AgreementsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/schemas/{tenantSchema}/agreements
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AgreementsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/schemas/{tenantSchema}/agreements", path_parameters)
    
    def by_agreement_no(self,agreement_no: str) -> WithAgreementNoItemRequestBuilder:
        """
        Gets an item from the clients.leasesoft_api.api.schemas.item.agreements.item collection
        param agreement_no: Unique identifier of the item
        Returns: WithAgreementNoItemRequestBuilder
        """
        if agreement_no is None:
            raise TypeError("agreement_no cannot be null.")
        from .item.with_agreement_no_item_request_builder import WithAgreementNoItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["agreementNo"] = agreement_no
        return WithAgreementNoItemRequestBuilder(self.request_adapter, url_tpl_params)
    

