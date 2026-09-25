from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agreement.agreement_request_builder import AgreementRequestBuilder
    from .attachment.attachment_request_builder import AttachmentRequestBuilder

class EmailRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/document/email
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EmailRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/document/email", path_parameters)
    
    @property
    def agreement(self) -> AgreementRequestBuilder:
        """
        The agreement property
        """
        from .agreement.agreement_request_builder import AgreementRequestBuilder

        return AgreementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def attachment(self) -> AttachmentRequestBuilder:
        """
        The attachment property
        """
        from .attachment.attachment_request_builder import AttachmentRequestBuilder

        return AttachmentRequestBuilder(self.request_adapter, self.path_parameters)
    

