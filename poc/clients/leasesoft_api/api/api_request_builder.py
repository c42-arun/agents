from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agreement.agreement_request_builder import AgreementRequestBuilder
    from .agreements.agreements_request_builder import AgreementsRequestBuilder
    from .agreements_in_underwriting.agreements_in_underwriting_request_builder import AgreementsInUnderwritingRequestBuilder
    from .brokers.brokers_request_builder import BrokersRequestBuilder
    from .collateral_document.collateral_document_request_builder import CollateralDocumentRequestBuilder
    from .datahub.datahub_request_builder import DatahubRequestBuilder
    from .document.document_request_builder import DocumentRequestBuilder
    from .documents.documents_request_builder import DocumentsRequestBuilder
    from .financial.financial_request_builder import FinancialRequestBuilder
    from .invoicecodes.invoicecodes_request_builder import InvoicecodesRequestBuilder
    from .live_agreement.live_agreement_request_builder import LiveAgreementRequestBuilder
    from .live_agreements.live_agreements_request_builder import LiveAgreementsRequestBuilder
    from .parties.parties_request_builder import PartiesRequestBuilder
    from .printers.printers_request_builder import PrintersRequestBuilder
    from .proposals.proposals_request_builder import ProposalsRequestBuilder
    from .schemas.schemas_request_builder import SchemasRequestBuilder
    from .transactions.transactions_request_builder import TransactionsRequestBuilder
    from .transaction_details.transaction_details_request_builder import TransactionDetailsRequestBuilder
    from .vehicle.vehicle_request_builder import VehicleRequestBuilder

class ApiRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ApiRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api", path_parameters)
    
    @property
    def agreement(self) -> AgreementRequestBuilder:
        """
        The agreement property
        """
        from .agreement.agreement_request_builder import AgreementRequestBuilder

        return AgreementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def agreements(self) -> AgreementsRequestBuilder:
        """
        The agreements property
        """
        from .agreements.agreements_request_builder import AgreementsRequestBuilder

        return AgreementsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def agreements_in_underwriting(self) -> AgreementsInUnderwritingRequestBuilder:
        """
        The agreementsInUnderwriting property
        """
        from .agreements_in_underwriting.agreements_in_underwriting_request_builder import AgreementsInUnderwritingRequestBuilder

        return AgreementsInUnderwritingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def brokers(self) -> BrokersRequestBuilder:
        """
        The Brokers property
        """
        from .brokers.brokers_request_builder import BrokersRequestBuilder

        return BrokersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def collateral_document(self) -> CollateralDocumentRequestBuilder:
        """
        The collateralDocument property
        """
        from .collateral_document.collateral_document_request_builder import CollateralDocumentRequestBuilder

        return CollateralDocumentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def datahub(self) -> DatahubRequestBuilder:
        """
        The datahub property
        """
        from .datahub.datahub_request_builder import DatahubRequestBuilder

        return DatahubRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def document(self) -> DocumentRequestBuilder:
        """
        The document property
        """
        from .document.document_request_builder import DocumentRequestBuilder

        return DocumentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def documents(self) -> DocumentsRequestBuilder:
        """
        The documents property
        """
        from .documents.documents_request_builder import DocumentsRequestBuilder

        return DocumentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def financial(self) -> FinancialRequestBuilder:
        """
        The financial property
        """
        from .financial.financial_request_builder import FinancialRequestBuilder

        return FinancialRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def invoicecodes(self) -> InvoicecodesRequestBuilder:
        """
        The invoicecodes property
        """
        from .invoicecodes.invoicecodes_request_builder import InvoicecodesRequestBuilder

        return InvoicecodesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def live_agreement(self) -> LiveAgreementRequestBuilder:
        """
        The liveAgreement property
        """
        from .live_agreement.live_agreement_request_builder import LiveAgreementRequestBuilder

        return LiveAgreementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def live_agreements(self) -> LiveAgreementsRequestBuilder:
        """
        The liveAgreements property
        """
        from .live_agreements.live_agreements_request_builder import LiveAgreementsRequestBuilder

        return LiveAgreementsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def parties(self) -> PartiesRequestBuilder:
        """
        The parties property
        """
        from .parties.parties_request_builder import PartiesRequestBuilder

        return PartiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def printers(self) -> PrintersRequestBuilder:
        """
        The printers property
        """
        from .printers.printers_request_builder import PrintersRequestBuilder

        return PrintersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def proposals(self) -> ProposalsRequestBuilder:
        """
        The Proposals property
        """
        from .proposals.proposals_request_builder import ProposalsRequestBuilder

        return ProposalsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def schemas(self) -> SchemasRequestBuilder:
        """
        The schemas property
        """
        from .schemas.schemas_request_builder import SchemasRequestBuilder

        return SchemasRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transaction_details(self) -> TransactionDetailsRequestBuilder:
        """
        The transactionDetails property
        """
        from .transaction_details.transaction_details_request_builder import TransactionDetailsRequestBuilder

        return TransactionDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transactions(self) -> TransactionsRequestBuilder:
        """
        The transactions property
        """
        from .transactions.transactions_request_builder import TransactionsRequestBuilder

        return TransactionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vehicle(self) -> VehicleRequestBuilder:
        """
        The vehicle property
        """
        from .vehicle.vehicle_request_builder import VehicleRequestBuilder

        return VehicleRequestBuilder(self.request_adapter, self.path_parameters)
    

