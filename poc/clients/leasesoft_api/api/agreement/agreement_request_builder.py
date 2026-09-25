from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .asset_details.asset_details_request_builder import AssetDetailsRequestBuilder
    from .collateral_documents.collateral_documents_request_builder import CollateralDocumentsRequestBuilder
    from .details.details_request_builder import DetailsRequestBuilder
    from .item.with_agreement_no_item_request_builder import WithAgreementNoItemRequestBuilder
    from .notes.notes_request_builder import NotesRequestBuilder
    from .primary_contact_details.primary_contact_details_request_builder import PrimaryContactDetailsRequestBuilder
    from .quickload.quickload_request_builder import QuickloadRequestBuilder

class AgreementRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/agreement
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AgreementRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/agreement", path_parameters)
    
    def by_agreement_no(self,agreement_no: str) -> WithAgreementNoItemRequestBuilder:
        """
        Gets an item from the clients.leasesoft_api.api.agreement.item collection
        param agreement_no: Unique identifier of the item
        Returns: WithAgreementNoItemRequestBuilder
        """
        if agreement_no is None:
            raise TypeError("agreement_no cannot be null.")
        from .item.with_agreement_no_item_request_builder import WithAgreementNoItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["agreementNo"] = agreement_no
        return WithAgreementNoItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def asset_details(self) -> AssetDetailsRequestBuilder:
        """
        The assetDetails property
        """
        from .asset_details.asset_details_request_builder import AssetDetailsRequestBuilder

        return AssetDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def collateral_documents(self) -> CollateralDocumentsRequestBuilder:
        """
        The collateralDocuments property
        """
        from .collateral_documents.collateral_documents_request_builder import CollateralDocumentsRequestBuilder

        return CollateralDocumentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def details(self) -> DetailsRequestBuilder:
        """
        The details property
        """
        from .details.details_request_builder import DetailsRequestBuilder

        return DetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def notes(self) -> NotesRequestBuilder:
        """
        The notes property
        """
        from .notes.notes_request_builder import NotesRequestBuilder

        return NotesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def primary_contact_details(self) -> PrimaryContactDetailsRequestBuilder:
        """
        The primaryContactDetails property
        """
        from .primary_contact_details.primary_contact_details_request_builder import PrimaryContactDetailsRequestBuilder

        return PrimaryContactDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def quickload(self) -> QuickloadRequestBuilder:
        """
        The quickload property
        """
        from .quickload.quickload_request_builder import QuickloadRequestBuilder

        return QuickloadRequestBuilder(self.request_adapter, self.path_parameters)
    

