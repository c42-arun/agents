from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_agreement_number_item_request_builder import WithAgreementNumberItemRequestBuilder

class AgreementRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/document/email/agreement
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AgreementRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/document/email/agreement", path_parameters)
    
    def by_agreement_number(self,agreement_number: str) -> WithAgreementNumberItemRequestBuilder:
        """
        Gets an item from the clients.leasesoft_api.api.document.email.agreement.item collection
        param agreement_number: Unique identifier of the item
        Returns: WithAgreementNumberItemRequestBuilder
        """
        if agreement_number is None:
            raise TypeError("agreement_number cannot be null.")
        from .item.with_agreement_number_item_request_builder import WithAgreementNumberItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["agreementNumber"] = agreement_number
        return WithAgreementNumberItemRequestBuilder(self.request_adapter, url_tpl_params)
    

