from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .assets.assets_request_builder import AssetsRequestBuilder
    from .settlement_upgrade_quotes.settlement_upgrade_quotes_request_builder import SettlementUpgradeQuotesRequestBuilder
    from .verify_broker_shortname.verify_broker_shortname_request_builder import VerifyBrokerShortnameRequestBuilder
    from .verify_last_asset_supplier_shortname.verify_last_asset_supplier_shortname_request_builder import VerifyLastAssetSupplierShortnameRequestBuilder

class WithAgreementNoItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/schemas/{tenantSchema}/agreements/{agreementNo}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithAgreementNoItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/schemas/{tenantSchema}/agreements/{agreementNo}", path_parameters)
    
    @property
    def assets(self) -> AssetsRequestBuilder:
        """
        The assets property
        """
        from .assets.assets_request_builder import AssetsRequestBuilder

        return AssetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settlement_upgrade_quotes(self) -> SettlementUpgradeQuotesRequestBuilder:
        """
        The settlementUpgradeQuotes property
        """
        from .settlement_upgrade_quotes.settlement_upgrade_quotes_request_builder import SettlementUpgradeQuotesRequestBuilder

        return SettlementUpgradeQuotesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def verify_broker_shortname(self) -> VerifyBrokerShortnameRequestBuilder:
        """
        The verifyBrokerShortname property
        """
        from .verify_broker_shortname.verify_broker_shortname_request_builder import VerifyBrokerShortnameRequestBuilder

        return VerifyBrokerShortnameRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def verify_last_asset_supplier_shortname(self) -> VerifyLastAssetSupplierShortnameRequestBuilder:
        """
        The verifyLastAssetSupplierShortname property
        """
        from .verify_last_asset_supplier_shortname.verify_last_asset_supplier_shortname_request_builder import VerifyLastAssetSupplierShortnameRequestBuilder

        return VerifyLastAssetSupplierShortnameRequestBuilder(self.request_adapter, self.path_parameters)
    

