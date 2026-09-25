from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agreements.agreements_request_builder import AgreementsRequestBuilder
    from .asset_types.asset_types_request_builder import AssetTypesRequestBuilder
    from .edi_message.edi_message_request_builder import EdiMessageRequestBuilder
    from .edi_request.edi_request_request_builder import EdiRequestRequestBuilder
    from .legal_entity_types.legal_entity_types_request_builder import LegalEntityTypesRequestBuilder
    from .loan_equipment_types.loan_equipment_types_request_builder import LoanEquipmentTypesRequestBuilder
    from .product_types.product_types_request_builder import ProductTypesRequestBuilder
    from .repayment_account_bank_details.repayment_account_bank_details_request_builder import RepaymentAccountBankDetailsRequestBuilder
    from .repayment_frequencies.repayment_frequencies_request_builder import RepaymentFrequenciesRequestBuilder
    from .school_equipment_types.school_equipment_types_request_builder import SchoolEquipmentTypesRequestBuilder
    from .sic_codes.sic_codes_request_builder import SicCodesRequestBuilder
    from .suppliers.suppliers_request_builder import SuppliersRequestBuilder
    from .titles.titles_request_builder import TitlesRequestBuilder

class WithTenantSchemaItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/schemas/{tenantSchema}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithTenantSchemaItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/schemas/{tenantSchema}", path_parameters)
    
    @property
    def agreements(self) -> AgreementsRequestBuilder:
        """
        The agreements property
        """
        from .agreements.agreements_request_builder import AgreementsRequestBuilder

        return AgreementsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def asset_types(self) -> AssetTypesRequestBuilder:
        """
        The assetTypes property
        """
        from .asset_types.asset_types_request_builder import AssetTypesRequestBuilder

        return AssetTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def edi_message(self) -> EdiMessageRequestBuilder:
        """
        The ediMessage property
        """
        from .edi_message.edi_message_request_builder import EdiMessageRequestBuilder

        return EdiMessageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def edi_request(self) -> EdiRequestRequestBuilder:
        """
        The ediRequest property
        """
        from .edi_request.edi_request_request_builder import EdiRequestRequestBuilder

        return EdiRequestRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def legal_entity_types(self) -> LegalEntityTypesRequestBuilder:
        """
        The legalEntityTypes property
        """
        from .legal_entity_types.legal_entity_types_request_builder import LegalEntityTypesRequestBuilder

        return LegalEntityTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def loan_equipment_types(self) -> LoanEquipmentTypesRequestBuilder:
        """
        The loanEquipmentTypes property
        """
        from .loan_equipment_types.loan_equipment_types_request_builder import LoanEquipmentTypesRequestBuilder

        return LoanEquipmentTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def product_types(self) -> ProductTypesRequestBuilder:
        """
        The productTypes property
        """
        from .product_types.product_types_request_builder import ProductTypesRequestBuilder

        return ProductTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def repayment_account_bank_details(self) -> RepaymentAccountBankDetailsRequestBuilder:
        """
        The repaymentAccountBankDetails property
        """
        from .repayment_account_bank_details.repayment_account_bank_details_request_builder import RepaymentAccountBankDetailsRequestBuilder

        return RepaymentAccountBankDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def repayment_frequencies(self) -> RepaymentFrequenciesRequestBuilder:
        """
        The repaymentFrequencies property
        """
        from .repayment_frequencies.repayment_frequencies_request_builder import RepaymentFrequenciesRequestBuilder

        return RepaymentFrequenciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def school_equipment_types(self) -> SchoolEquipmentTypesRequestBuilder:
        """
        The schoolEquipmentTypes property
        """
        from .school_equipment_types.school_equipment_types_request_builder import SchoolEquipmentTypesRequestBuilder

        return SchoolEquipmentTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sic_codes(self) -> SicCodesRequestBuilder:
        """
        The sicCodes property
        """
        from .sic_codes.sic_codes_request_builder import SicCodesRequestBuilder

        return SicCodesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def suppliers(self) -> SuppliersRequestBuilder:
        """
        The suppliers property
        """
        from .suppliers.suppliers_request_builder import SuppliersRequestBuilder

        return SuppliersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def titles(self) -> TitlesRequestBuilder:
        """
        The titles property
        """
        from .titles.titles_request_builder import TitlesRequestBuilder

        return TitlesRequestBuilder(self.request_adapter, self.path_parameters)
    

