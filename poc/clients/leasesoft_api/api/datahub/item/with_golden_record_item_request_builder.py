from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agreement.agreement_request_builder import AgreementRequestBuilder
    from .agreements.agreements_request_builder import AgreementsRequestBuilder
    from .document.document_request_builder import DocumentRequestBuilder
    from .invoices.invoices_request_builder import InvoicesRequestBuilder
    from .transactions.transactions_request_builder import TransactionsRequestBuilder

class WithGoldenRecordItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/datahub/{goldenRecordId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithGoldenRecordItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/datahub/{goldenRecordId}", path_parameters)
    
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
    def document(self) -> DocumentRequestBuilder:
        """
        The document property
        """
        from .document.document_request_builder import DocumentRequestBuilder

        return DocumentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def invoices(self) -> InvoicesRequestBuilder:
        """
        The invoices property
        """
        from .invoices.invoices_request_builder import InvoicesRequestBuilder

        return InvoicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transactions(self) -> TransactionsRequestBuilder:
        """
        The transactions property
        """
        from .transactions.transactions_request_builder import TransactionsRequestBuilder

        return TransactionsRequestBuilder(self.request_adapter, self.path_parameters)
    

