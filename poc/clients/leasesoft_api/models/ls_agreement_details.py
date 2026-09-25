from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ls_other_cost import LsOtherCost

@dataclass
class LsAgreementDetails(Parsable):
    # The additionalInformation property
    additional_information: Optional[int] = None
    # The additionalSecurityFlag property
    additional_security_flag: Optional[str] = None
    # The additionalSecurityTaken property
    additional_security_taken: Optional[str] = None
    # The analysisCode1 property
    analysis_code1: Optional[str] = None
    # The analysisCode2 property
    analysis_code2: Optional[str] = None
    # The analysisCode3 property
    analysis_code3: Optional[str] = None
    # The analysisCode4 property
    analysis_code4: Optional[str] = None
    # The analysisCode5 property
    analysis_code5: Optional[str] = None
    # The analysisCode6 property
    analysis_code6: Optional[str] = None
    # The analysisCode7 property
    analysis_code7: Optional[str] = None
    # The analysisCode8 property
    analysis_code8: Optional[str] = None
    # The arrearsAmount property
    arrears_amount: Optional[float] = None
    # The arrearsReason property
    arrears_reason: Optional[str] = None
    # The arrearsReasonCode property
    arrears_reason_code: Optional[str] = None
    # The assetCost property
    asset_cost: Optional[float] = None
    # The assetDescription property
    asset_description: Optional[str] = None
    # The assetTypeCode property
    asset_type_code: Optional[int] = None
    # The assetTypeDescription property
    asset_type_description: Optional[str] = None
    # The assetVat property
    asset_vat: Optional[float] = None
    # The badPayerFlag property
    bad_payer_flag: Optional[int] = None
    # The bdpArrears property
    bdp_arrears: Optional[float] = None
    # The branch property
    branch: Optional[str] = None
    # The branchCode property
    branch_code: Optional[str] = None
    # The calculatedApr property
    calculated_apr: Optional[float] = None
    # The calculatedLoanToValue property
    calculated_loan_to_value: Optional[float] = None
    # The caseType property
    case_type: Optional[str] = None
    # The collections property
    collections: Optional[str] = None
    # The contractNumber property
    contract_number: Optional[str] = None
    # The contractType property
    contract_type: Optional[str] = None
    # The contractTypeCode property
    contract_type_code: Optional[str] = None
    # The currencyCode property
    currency_code: Optional[str] = None
    # The documentSet property
    document_set: Optional[str] = None
    # The documentSetCode property
    document_set_code: Optional[str] = None
    # The documentation property
    documentation: Optional[str] = None
    # The documentationSource property
    documentation_source: Optional[str] = None
    # The endDate property
    end_date: Optional[datetime.datetime] = None
    # The equipmentType property
    equipment_type: Optional[str] = None
    # The externalReference property
    external_reference: Optional[str] = None
    # The formulaBadDebtProvision property
    formula_bad_debt_provision: Optional[float] = None
    # The fundingMethod property
    funding_method: Optional[str] = None
    # The genericProductCode property
    generic_product_code: Optional[str] = None
    # The genericProductType property
    generic_product_type: Optional[str] = None
    # The grossYield property
    gross_yield: Optional[float] = None
    # The guaranteeedBuyBack property
    guaranteeed_buy_back: Optional[float] = None
    # The hardOrSoftAsset property
    hard_or_soft_asset: Optional[int] = None
    # The ignoreLatePayments property
    ignore_late_payments: Optional[int] = None
    # The interestFixedOrVariable property
    interest_fixed_or_variable: Optional[str] = None
    # The investecCompanyCode property
    investec_company_code: Optional[str] = None
    # The invoiceChainAgreement property
    invoice_chain_agreement: Optional[int] = None
    # The latePaymentCounter property
    late_payment_counter: Optional[int] = None
    # The lessorDeposit3 property
    lessor_deposit3: Optional[float] = None
    # The lessorDeposit4 property
    lessor_deposit4: Optional[float] = None
    # The loanEquipmentCode property
    loan_equipment_code: Optional[str] = None
    # The marketing property
    marketing: Optional[str] = None
    # The netYield property
    net_yield: Optional[float] = None
    # The noOfGuarantees property
    no_of_guarantees: Optional[int] = None
    # The numberOfYearsTrading property
    number_of_years_trading: Optional[str] = None
    # The opAware property
    op_aware: Optional[str] = None
    # The opID property
    op_i_d: Optional[str] = None
    # The operator property
    operator: Optional[str] = None
    # The otherCaptialCosts2 property
    other_captial_costs2: Optional[float] = None
    # The otherCaptialCosts3 property
    other_captial_costs3: Optional[float] = None
    # The otherCostCode property
    other_cost_code: Optional[str] = None
    # The otherCostType property
    other_cost_type: Optional[str] = None
    # The otherCosts property
    other_costs: Optional[list[LsOtherCost]] = None
    # The otherCostsTotal property
    other_costs_total: Optional[float] = None
    # The paymentMethod property
    payment_method: Optional[str] = None
    # The paymentMethodCode property
    payment_method_code: Optional[str] = None
    # The period property
    period: Optional[int] = None
    # The profile property
    profile: Optional[str] = None
    # The qualityCategory property
    quality_category: Optional[str] = None
    # The receivedDate property
    received_date: Optional[datetime.datetime] = None
    # The regulatedBy property
    regulated_by: Optional[str] = None
    # The regulatedCode property
    regulated_code: Optional[int] = None
    # The rentalFrequencyCode property
    rental_frequency_code: Optional[str] = None
    # The residualValue property
    residual_value: Optional[float] = None
    # The rqmeResponseData property
    rqme_response_data: Optional[str] = None
    # The schemeCode property
    scheme_code: Optional[str] = None
    # The schemeDescription property
    scheme_description: Optional[str] = None
    # The setLiveDate property
    set_live_date: Optional[datetime.datetime] = None
    # The specificBadDebtProvision property
    specific_bad_debt_provision: Optional[float] = None
    # The startDate property
    start_date: Optional[datetime.datetime] = None
    # The status property
    status: Optional[str] = None
    # The statusCode property
    status_code: Optional[str] = None
    # The subStatus property
    sub_status: Optional[str] = None
    # The subStatusCode property
    sub_status_code: Optional[str] = None
    # The supplierDeposit property
    supplier_deposit: Optional[float] = None
    # The supplierDeposit2 property
    supplier_deposit2: Optional[float] = None
    # The undisclosedAgency property
    undisclosed_agency: Optional[str] = None
    # The undisclosedAgencyCode property
    undisclosed_agency_code: Optional[str] = None
    # The undisclosedContractType property
    undisclosed_contract_type: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsAgreementDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsAgreementDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsAgreementDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ls_other_cost import LsOtherCost

        from .ls_other_cost import LsOtherCost

        fields: dict[str, Callable[[Any], None]] = {
            "additionalInformation": lambda n : setattr(self, 'additional_information', n.get_int_value()),
            "additionalSecurityFlag": lambda n : setattr(self, 'additional_security_flag', n.get_str_value()),
            "additionalSecurityTaken": lambda n : setattr(self, 'additional_security_taken', n.get_str_value()),
            "analysisCode1": lambda n : setattr(self, 'analysis_code1', n.get_str_value()),
            "analysisCode2": lambda n : setattr(self, 'analysis_code2', n.get_str_value()),
            "analysisCode3": lambda n : setattr(self, 'analysis_code3', n.get_str_value()),
            "analysisCode4": lambda n : setattr(self, 'analysis_code4', n.get_str_value()),
            "analysisCode5": lambda n : setattr(self, 'analysis_code5', n.get_str_value()),
            "analysisCode6": lambda n : setattr(self, 'analysis_code6', n.get_str_value()),
            "analysisCode7": lambda n : setattr(self, 'analysis_code7', n.get_str_value()),
            "analysisCode8": lambda n : setattr(self, 'analysis_code8', n.get_str_value()),
            "arrearsAmount": lambda n : setattr(self, 'arrears_amount', n.get_float_value()),
            "arrearsReason": lambda n : setattr(self, 'arrears_reason', n.get_str_value()),
            "arrearsReasonCode": lambda n : setattr(self, 'arrears_reason_code', n.get_str_value()),
            "assetCost": lambda n : setattr(self, 'asset_cost', n.get_float_value()),
            "assetDescription": lambda n : setattr(self, 'asset_description', n.get_str_value()),
            "assetTypeCode": lambda n : setattr(self, 'asset_type_code', n.get_int_value()),
            "assetTypeDescription": lambda n : setattr(self, 'asset_type_description', n.get_str_value()),
            "assetVat": lambda n : setattr(self, 'asset_vat', n.get_float_value()),
            "badPayerFlag": lambda n : setattr(self, 'bad_payer_flag', n.get_int_value()),
            "bdpArrears": lambda n : setattr(self, 'bdp_arrears', n.get_float_value()),
            "branch": lambda n : setattr(self, 'branch', n.get_str_value()),
            "branchCode": lambda n : setattr(self, 'branch_code', n.get_str_value()),
            "calculatedApr": lambda n : setattr(self, 'calculated_apr', n.get_float_value()),
            "calculatedLoanToValue": lambda n : setattr(self, 'calculated_loan_to_value', n.get_float_value()),
            "caseType": lambda n : setattr(self, 'case_type', n.get_str_value()),
            "collections": lambda n : setattr(self, 'collections', n.get_str_value()),
            "contractNumber": lambda n : setattr(self, 'contract_number', n.get_str_value()),
            "contractType": lambda n : setattr(self, 'contract_type', n.get_str_value()),
            "contractTypeCode": lambda n : setattr(self, 'contract_type_code', n.get_str_value()),
            "currencyCode": lambda n : setattr(self, 'currency_code', n.get_str_value()),
            "documentSet": lambda n : setattr(self, 'document_set', n.get_str_value()),
            "documentSetCode": lambda n : setattr(self, 'document_set_code', n.get_str_value()),
            "documentation": lambda n : setattr(self, 'documentation', n.get_str_value()),
            "documentationSource": lambda n : setattr(self, 'documentation_source', n.get_str_value()),
            "endDate": lambda n : setattr(self, 'end_date', n.get_datetime_value()),
            "equipmentType": lambda n : setattr(self, 'equipment_type', n.get_str_value()),
            "externalReference": lambda n : setattr(self, 'external_reference', n.get_str_value()),
            "formulaBadDebtProvision": lambda n : setattr(self, 'formula_bad_debt_provision', n.get_float_value()),
            "fundingMethod": lambda n : setattr(self, 'funding_method', n.get_str_value()),
            "genericProductCode": lambda n : setattr(self, 'generic_product_code', n.get_str_value()),
            "genericProductType": lambda n : setattr(self, 'generic_product_type', n.get_str_value()),
            "grossYield": lambda n : setattr(self, 'gross_yield', n.get_float_value()),
            "guaranteeedBuyBack": lambda n : setattr(self, 'guaranteeed_buy_back', n.get_float_value()),
            "hardOrSoftAsset": lambda n : setattr(self, 'hard_or_soft_asset', n.get_int_value()),
            "ignoreLatePayments": lambda n : setattr(self, 'ignore_late_payments', n.get_int_value()),
            "interestFixedOrVariable": lambda n : setattr(self, 'interest_fixed_or_variable', n.get_str_value()),
            "investecCompanyCode": lambda n : setattr(self, 'investec_company_code', n.get_str_value()),
            "invoiceChainAgreement": lambda n : setattr(self, 'invoice_chain_agreement', n.get_int_value()),
            "latePaymentCounter": lambda n : setattr(self, 'late_payment_counter', n.get_int_value()),
            "lessorDeposit3": lambda n : setattr(self, 'lessor_deposit3', n.get_float_value()),
            "lessorDeposit4": lambda n : setattr(self, 'lessor_deposit4', n.get_float_value()),
            "loanEquipmentCode": lambda n : setattr(self, 'loan_equipment_code', n.get_str_value()),
            "marketing": lambda n : setattr(self, 'marketing', n.get_str_value()),
            "netYield": lambda n : setattr(self, 'net_yield', n.get_float_value()),
            "noOfGuarantees": lambda n : setattr(self, 'no_of_guarantees', n.get_int_value()),
            "numberOfYearsTrading": lambda n : setattr(self, 'number_of_years_trading', n.get_str_value()),
            "opAware": lambda n : setattr(self, 'op_aware', n.get_str_value()),
            "opID": lambda n : setattr(self, 'op_i_d', n.get_str_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_str_value()),
            "otherCaptialCosts2": lambda n : setattr(self, 'other_captial_costs2', n.get_float_value()),
            "otherCaptialCosts3": lambda n : setattr(self, 'other_captial_costs3', n.get_float_value()),
            "otherCostCode": lambda n : setattr(self, 'other_cost_code', n.get_str_value()),
            "otherCostType": lambda n : setattr(self, 'other_cost_type', n.get_str_value()),
            "otherCosts": lambda n : setattr(self, 'other_costs', n.get_collection_of_object_values(LsOtherCost)),
            "otherCostsTotal": lambda n : setattr(self, 'other_costs_total', n.get_float_value()),
            "paymentMethod": lambda n : setattr(self, 'payment_method', n.get_str_value()),
            "paymentMethodCode": lambda n : setattr(self, 'payment_method_code', n.get_str_value()),
            "period": lambda n : setattr(self, 'period', n.get_int_value()),
            "profile": lambda n : setattr(self, 'profile', n.get_str_value()),
            "qualityCategory": lambda n : setattr(self, 'quality_category', n.get_str_value()),
            "receivedDate": lambda n : setattr(self, 'received_date', n.get_datetime_value()),
            "regulatedBy": lambda n : setattr(self, 'regulated_by', n.get_str_value()),
            "regulatedCode": lambda n : setattr(self, 'regulated_code', n.get_int_value()),
            "rentalFrequencyCode": lambda n : setattr(self, 'rental_frequency_code', n.get_str_value()),
            "residualValue": lambda n : setattr(self, 'residual_value', n.get_float_value()),
            "rqmeResponseData": lambda n : setattr(self, 'rqme_response_data', n.get_str_value()),
            "schemeCode": lambda n : setattr(self, 'scheme_code', n.get_str_value()),
            "schemeDescription": lambda n : setattr(self, 'scheme_description', n.get_str_value()),
            "setLiveDate": lambda n : setattr(self, 'set_live_date', n.get_datetime_value()),
            "specificBadDebtProvision": lambda n : setattr(self, 'specific_bad_debt_provision', n.get_float_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "statusCode": lambda n : setattr(self, 'status_code', n.get_str_value()),
            "subStatus": lambda n : setattr(self, 'sub_status', n.get_str_value()),
            "subStatusCode": lambda n : setattr(self, 'sub_status_code', n.get_str_value()),
            "supplierDeposit": lambda n : setattr(self, 'supplier_deposit', n.get_float_value()),
            "supplierDeposit2": lambda n : setattr(self, 'supplier_deposit2', n.get_float_value()),
            "undisclosedAgency": lambda n : setattr(self, 'undisclosed_agency', n.get_str_value()),
            "undisclosedAgencyCode": lambda n : setattr(self, 'undisclosed_agency_code', n.get_str_value()),
            "undisclosedContractType": lambda n : setattr(self, 'undisclosed_contract_type', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("additionalInformation", self.additional_information)
        writer.write_str_value("additionalSecurityFlag", self.additional_security_flag)
        writer.write_str_value("additionalSecurityTaken", self.additional_security_taken)
        writer.write_str_value("analysisCode1", self.analysis_code1)
        writer.write_str_value("analysisCode2", self.analysis_code2)
        writer.write_str_value("analysisCode3", self.analysis_code3)
        writer.write_str_value("analysisCode4", self.analysis_code4)
        writer.write_str_value("analysisCode5", self.analysis_code5)
        writer.write_str_value("analysisCode6", self.analysis_code6)
        writer.write_str_value("analysisCode7", self.analysis_code7)
        writer.write_str_value("analysisCode8", self.analysis_code8)
        writer.write_float_value("arrearsAmount", self.arrears_amount)
        writer.write_str_value("arrearsReason", self.arrears_reason)
        writer.write_str_value("arrearsReasonCode", self.arrears_reason_code)
        writer.write_float_value("assetCost", self.asset_cost)
        writer.write_str_value("assetDescription", self.asset_description)
        writer.write_int_value("assetTypeCode", self.asset_type_code)
        writer.write_str_value("assetTypeDescription", self.asset_type_description)
        writer.write_float_value("assetVat", self.asset_vat)
        writer.write_int_value("badPayerFlag", self.bad_payer_flag)
        writer.write_float_value("bdpArrears", self.bdp_arrears)
        writer.write_str_value("branch", self.branch)
        writer.write_str_value("branchCode", self.branch_code)
        writer.write_float_value("calculatedApr", self.calculated_apr)
        writer.write_float_value("calculatedLoanToValue", self.calculated_loan_to_value)
        writer.write_str_value("caseType", self.case_type)
        writer.write_str_value("collections", self.collections)
        writer.write_str_value("contractNumber", self.contract_number)
        writer.write_str_value("contractType", self.contract_type)
        writer.write_str_value("contractTypeCode", self.contract_type_code)
        writer.write_str_value("currencyCode", self.currency_code)
        writer.write_str_value("documentSet", self.document_set)
        writer.write_str_value("documentSetCode", self.document_set_code)
        writer.write_str_value("documentation", self.documentation)
        writer.write_str_value("documentationSource", self.documentation_source)
        writer.write_datetime_value("endDate", self.end_date)
        writer.write_str_value("equipmentType", self.equipment_type)
        writer.write_str_value("externalReference", self.external_reference)
        writer.write_float_value("formulaBadDebtProvision", self.formula_bad_debt_provision)
        writer.write_str_value("fundingMethod", self.funding_method)
        writer.write_str_value("genericProductCode", self.generic_product_code)
        writer.write_str_value("genericProductType", self.generic_product_type)
        writer.write_float_value("grossYield", self.gross_yield)
        writer.write_float_value("guaranteeedBuyBack", self.guaranteeed_buy_back)
        writer.write_int_value("hardOrSoftAsset", self.hard_or_soft_asset)
        writer.write_int_value("ignoreLatePayments", self.ignore_late_payments)
        writer.write_str_value("interestFixedOrVariable", self.interest_fixed_or_variable)
        writer.write_str_value("investecCompanyCode", self.investec_company_code)
        writer.write_int_value("invoiceChainAgreement", self.invoice_chain_agreement)
        writer.write_int_value("latePaymentCounter", self.late_payment_counter)
        writer.write_float_value("lessorDeposit3", self.lessor_deposit3)
        writer.write_float_value("lessorDeposit4", self.lessor_deposit4)
        writer.write_str_value("loanEquipmentCode", self.loan_equipment_code)
        writer.write_str_value("marketing", self.marketing)
        writer.write_float_value("netYield", self.net_yield)
        writer.write_int_value("noOfGuarantees", self.no_of_guarantees)
        writer.write_str_value("numberOfYearsTrading", self.number_of_years_trading)
        writer.write_str_value("opAware", self.op_aware)
        writer.write_str_value("opID", self.op_i_d)
        writer.write_str_value("operator", self.operator)
        writer.write_float_value("otherCaptialCosts2", self.other_captial_costs2)
        writer.write_float_value("otherCaptialCosts3", self.other_captial_costs3)
        writer.write_str_value("otherCostCode", self.other_cost_code)
        writer.write_str_value("otherCostType", self.other_cost_type)
        writer.write_collection_of_object_values("otherCosts", self.other_costs)
        writer.write_float_value("otherCostsTotal", self.other_costs_total)
        writer.write_str_value("paymentMethod", self.payment_method)
        writer.write_str_value("paymentMethodCode", self.payment_method_code)
        writer.write_int_value("period", self.period)
        writer.write_str_value("profile", self.profile)
        writer.write_str_value("qualityCategory", self.quality_category)
        writer.write_datetime_value("receivedDate", self.received_date)
        writer.write_str_value("regulatedBy", self.regulated_by)
        writer.write_int_value("regulatedCode", self.regulated_code)
        writer.write_str_value("rentalFrequencyCode", self.rental_frequency_code)
        writer.write_float_value("residualValue", self.residual_value)
        writer.write_str_value("rqmeResponseData", self.rqme_response_data)
        writer.write_str_value("schemeCode", self.scheme_code)
        writer.write_str_value("schemeDescription", self.scheme_description)
        writer.write_datetime_value("setLiveDate", self.set_live_date)
        writer.write_float_value("specificBadDebtProvision", self.specific_bad_debt_provision)
        writer.write_datetime_value("startDate", self.start_date)
        writer.write_str_value("status", self.status)
        writer.write_str_value("statusCode", self.status_code)
        writer.write_str_value("subStatus", self.sub_status)
        writer.write_str_value("subStatusCode", self.sub_status_code)
        writer.write_float_value("supplierDeposit", self.supplier_deposit)
        writer.write_float_value("supplierDeposit2", self.supplier_deposit2)
        writer.write_str_value("undisclosedAgency", self.undisclosed_agency)
        writer.write_str_value("undisclosedAgencyCode", self.undisclosed_agency_code)
        writer.write_int_value("undisclosedContractType", self.undisclosed_contract_type)
    

