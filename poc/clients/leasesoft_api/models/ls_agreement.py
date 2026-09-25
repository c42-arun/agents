from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ls_address import LsAddress
    from .ls_bank_details import LsBankDetails
    from .ls_business_line import LsBusinessLine
    from .ls_contact_details import LsContactDetails
    from .ls_customer_summary import LsCustomerSummary
    from .ls_insurer_details import LsInsurerDetails
    from .ls_payment_details import LsPaymentDetails
    from .ls_requester import LsRequester

@dataclass
class LsAgreement(Parsable):
    # The ageInMonths property
    age_in_months: Optional[int] = None
    # The agreementNo property
    agreement_no: Optional[str] = None
    # The allowActions property
    allow_actions: Optional[bool] = None
    # The amountBorrowed property
    amount_borrowed: Optional[float] = None
    # The arrearsValue property
    arrears_value: Optional[float] = None
    # The balance property
    balance: Optional[float] = None
    # The bankDetails property
    bank_details: Optional[LsBankDetails] = None
    # The brokerCompanyName property
    broker_company_name: Optional[str] = None
    # The brokerReference property
    broker_reference: Optional[str] = None
    # The businessContactDetails property
    business_contact_details: Optional[LsContactDetails] = None
    # The businessLine property
    business_line: Optional[LsBusinessLine] = None
    # The contractType property
    contract_type: Optional[str] = None
    # The contractTypeCode property
    contract_type_code: Optional[str] = None
    # The customer property
    customer: Optional[LsCustomerSummary] = None
    # The description property
    description: Optional[str] = None
    # The directDebitStatus property
    direct_debit_status: Optional[str] = None
    # The duration property
    duration: Optional[int] = None
    # The finalPayment property
    final_payment: Optional[LsPaymentDetails] = None
    # The insurer property
    insurer: Optional[LsInsurerDetails] = None
    # The interestRate property
    interest_rate: Optional[float] = None
    # The invoiceAddress property
    invoice_address: Optional[LsAddress] = None
    # The isEnded property
    is_ended: Optional[bool] = None
    # The isRegulated property
    is_regulated: Optional[bool] = None
    # The nextPayment property
    next_payment: Optional[LsPaymentDetails] = None
    # The optionToPurchaseFee property
    option_to_purchase_fee: Optional[float] = None
    # The primaryContactDetails property
    primary_contact_details: Optional[list[LsContactDetails]] = None
    # The registeredAddress property
    registered_address: Optional[LsAddress] = None
    # The remainingTermInMonths property
    remaining_term_in_months: Optional[int] = None
    # The repaymentAccountCode property
    repayment_account_code: Optional[str] = None
    # The repaymentCycle property
    repayment_cycle: Optional[str] = None
    # The requester property
    requester: Optional[LsRequester] = None
    # The settlementDate property
    settlement_date: Optional[datetime.datetime] = None
    # The settlementMethod property
    settlement_method: Optional[str] = None
    # The settlementMethodCode property
    settlement_method_code: Optional[str] = None
    # The startDate property
    start_date: Optional[datetime.datetime] = None
    # The statusCode property
    status_code: Optional[str] = None
    # The statusDescription property
    status_description: Optional[str] = None
    # The supplier property
    supplier: Optional[str] = None
    # The tenantSchema property
    tenant_schema: Optional[str] = None
    # The terminationDate property
    termination_date: Optional[datetime.datetime] = None
    # The totalAmountPayable property
    total_amount_payable: Optional[float] = None
    # The tradingAddress property
    trading_address: Optional[LsAddress] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsAgreement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsAgreement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsAgreement()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ls_address import LsAddress
        from .ls_bank_details import LsBankDetails
        from .ls_business_line import LsBusinessLine
        from .ls_contact_details import LsContactDetails
        from .ls_customer_summary import LsCustomerSummary
        from .ls_insurer_details import LsInsurerDetails
        from .ls_payment_details import LsPaymentDetails
        from .ls_requester import LsRequester

        from .ls_address import LsAddress
        from .ls_bank_details import LsBankDetails
        from .ls_business_line import LsBusinessLine
        from .ls_contact_details import LsContactDetails
        from .ls_customer_summary import LsCustomerSummary
        from .ls_insurer_details import LsInsurerDetails
        from .ls_payment_details import LsPaymentDetails
        from .ls_requester import LsRequester

        fields: dict[str, Callable[[Any], None]] = {
            "ageInMonths": lambda n : setattr(self, 'age_in_months', n.get_int_value()),
            "agreementNo": lambda n : setattr(self, 'agreement_no', n.get_str_value()),
            "allowActions": lambda n : setattr(self, 'allow_actions', n.get_bool_value()),
            "amountBorrowed": lambda n : setattr(self, 'amount_borrowed', n.get_float_value()),
            "arrearsValue": lambda n : setattr(self, 'arrears_value', n.get_float_value()),
            "balance": lambda n : setattr(self, 'balance', n.get_float_value()),
            "bankDetails": lambda n : setattr(self, 'bank_details', n.get_object_value(LsBankDetails)),
            "brokerCompanyName": lambda n : setattr(self, 'broker_company_name', n.get_str_value()),
            "brokerReference": lambda n : setattr(self, 'broker_reference', n.get_str_value()),
            "businessContactDetails": lambda n : setattr(self, 'business_contact_details', n.get_object_value(LsContactDetails)),
            "businessLine": lambda n : setattr(self, 'business_line', n.get_enum_value(LsBusinessLine)),
            "contractType": lambda n : setattr(self, 'contract_type', n.get_str_value()),
            "contractTypeCode": lambda n : setattr(self, 'contract_type_code', n.get_str_value()),
            "customer": lambda n : setattr(self, 'customer', n.get_object_value(LsCustomerSummary)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "directDebitStatus": lambda n : setattr(self, 'direct_debit_status', n.get_str_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_int_value()),
            "finalPayment": lambda n : setattr(self, 'final_payment', n.get_object_value(LsPaymentDetails)),
            "insurer": lambda n : setattr(self, 'insurer', n.get_object_value(LsInsurerDetails)),
            "interestRate": lambda n : setattr(self, 'interest_rate', n.get_float_value()),
            "invoiceAddress": lambda n : setattr(self, 'invoice_address', n.get_object_value(LsAddress)),
            "isEnded": lambda n : setattr(self, 'is_ended', n.get_bool_value()),
            "isRegulated": lambda n : setattr(self, 'is_regulated', n.get_bool_value()),
            "nextPayment": lambda n : setattr(self, 'next_payment', n.get_object_value(LsPaymentDetails)),
            "optionToPurchaseFee": lambda n : setattr(self, 'option_to_purchase_fee', n.get_float_value()),
            "primaryContactDetails": lambda n : setattr(self, 'primary_contact_details', n.get_collection_of_object_values(LsContactDetails)),
            "registeredAddress": lambda n : setattr(self, 'registered_address', n.get_object_value(LsAddress)),
            "remainingTermInMonths": lambda n : setattr(self, 'remaining_term_in_months', n.get_int_value()),
            "repaymentAccountCode": lambda n : setattr(self, 'repayment_account_code', n.get_str_value()),
            "repaymentCycle": lambda n : setattr(self, 'repayment_cycle', n.get_str_value()),
            "requester": lambda n : setattr(self, 'requester', n.get_enum_value(LsRequester)),
            "settlementDate": lambda n : setattr(self, 'settlement_date', n.get_datetime_value()),
            "settlementMethod": lambda n : setattr(self, 'settlement_method', n.get_str_value()),
            "settlementMethodCode": lambda n : setattr(self, 'settlement_method_code', n.get_str_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_datetime_value()),
            "statusCode": lambda n : setattr(self, 'status_code', n.get_str_value()),
            "statusDescription": lambda n : setattr(self, 'status_description', n.get_str_value()),
            "supplier": lambda n : setattr(self, 'supplier', n.get_str_value()),
            "tenantSchema": lambda n : setattr(self, 'tenant_schema', n.get_str_value()),
            "terminationDate": lambda n : setattr(self, 'termination_date', n.get_datetime_value()),
            "totalAmountPayable": lambda n : setattr(self, 'total_amount_payable', n.get_float_value()),
            "tradingAddress": lambda n : setattr(self, 'trading_address', n.get_object_value(LsAddress)),
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
        writer.write_int_value("ageInMonths", self.age_in_months)
        writer.write_str_value("agreementNo", self.agreement_no)
        writer.write_bool_value("allowActions", self.allow_actions)
        writer.write_float_value("amountBorrowed", self.amount_borrowed)
        writer.write_float_value("arrearsValue", self.arrears_value)
        writer.write_float_value("balance", self.balance)
        writer.write_object_value("bankDetails", self.bank_details)
        writer.write_str_value("brokerCompanyName", self.broker_company_name)
        writer.write_str_value("brokerReference", self.broker_reference)
        writer.write_object_value("businessContactDetails", self.business_contact_details)
        writer.write_enum_value("businessLine", self.business_line)
        writer.write_str_value("contractType", self.contract_type)
        writer.write_str_value("contractTypeCode", self.contract_type_code)
        writer.write_object_value("customer", self.customer)
        writer.write_str_value("description", self.description)
        writer.write_str_value("directDebitStatus", self.direct_debit_status)
        writer.write_int_value("duration", self.duration)
        writer.write_object_value("finalPayment", self.final_payment)
        writer.write_object_value("insurer", self.insurer)
        writer.write_float_value("interestRate", self.interest_rate)
        writer.write_object_value("invoiceAddress", self.invoice_address)
        writer.write_bool_value("isEnded", self.is_ended)
        writer.write_bool_value("isRegulated", self.is_regulated)
        writer.write_object_value("nextPayment", self.next_payment)
        writer.write_float_value("optionToPurchaseFee", self.option_to_purchase_fee)
        writer.write_collection_of_object_values("primaryContactDetails", self.primary_contact_details)
        writer.write_object_value("registeredAddress", self.registered_address)
        writer.write_int_value("remainingTermInMonths", self.remaining_term_in_months)
        writer.write_str_value("repaymentAccountCode", self.repayment_account_code)
        writer.write_str_value("repaymentCycle", self.repayment_cycle)
        writer.write_enum_value("requester", self.requester)
        writer.write_datetime_value("settlementDate", self.settlement_date)
        writer.write_str_value("settlementMethod", self.settlement_method)
        writer.write_str_value("settlementMethodCode", self.settlement_method_code)
        writer.write_datetime_value("startDate", self.start_date)
        writer.write_str_value("statusCode", self.status_code)
        writer.write_str_value("statusDescription", self.status_description)
        writer.write_str_value("supplier", self.supplier)
        writer.write_str_value("tenantSchema", self.tenant_schema)
        writer.write_datetime_value("terminationDate", self.termination_date)
        writer.write_float_value("totalAmountPayable", self.total_amount_payable)
        writer.write_object_value("tradingAddress", self.trading_address)
    

