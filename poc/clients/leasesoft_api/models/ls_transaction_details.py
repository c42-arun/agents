from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsTransactionDetails(Parsable):
    # The amount property
    amount: Optional[float] = None
    # The balanceType property
    balance_type: Optional[str] = None
    # The bankRef property
    bank_ref: Optional[str] = None
    # The batchNumber property
    batch_number: Optional[int] = None
    # The contractNo property
    contract_no: Optional[str] = None
    # The currency property
    currency: Optional[str] = None
    # The decrease property
    decrease: Optional[float] = None
    # The description property
    description: Optional[str] = None
    # The direction property
    direction: Optional[int] = None
    # The increase property
    increase: Optional[float] = None
    # The processTypeCode property
    process_type_code: Optional[str] = None
    # The status property
    status: Optional[str] = None
    # The statusType property
    status_type: Optional[str] = None
    # The statusTypeCode property
    status_type_code: Optional[str] = None
    # The transactionAutocode property
    transaction_autocode: Optional[int] = None
    # The transactionReversal property
    transaction_reversal: Optional[int] = None
    # The transactionType property
    transaction_type: Optional[str] = None
    # The transactionTypeCode property
    transaction_type_code: Optional[str] = None
    # The valueDate property
    value_date: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsTransactionDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsTransactionDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsTransactionDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "amount": lambda n : setattr(self, 'amount', n.get_float_value()),
            "balanceType": lambda n : setattr(self, 'balance_type', n.get_str_value()),
            "bankRef": lambda n : setattr(self, 'bank_ref', n.get_str_value()),
            "batchNumber": lambda n : setattr(self, 'batch_number', n.get_int_value()),
            "contractNo": lambda n : setattr(self, 'contract_no', n.get_str_value()),
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "decrease": lambda n : setattr(self, 'decrease', n.get_float_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "direction": lambda n : setattr(self, 'direction', n.get_int_value()),
            "increase": lambda n : setattr(self, 'increase', n.get_float_value()),
            "processTypeCode": lambda n : setattr(self, 'process_type_code', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "statusType": lambda n : setattr(self, 'status_type', n.get_str_value()),
            "statusTypeCode": lambda n : setattr(self, 'status_type_code', n.get_str_value()),
            "transactionAutocode": lambda n : setattr(self, 'transaction_autocode', n.get_int_value()),
            "transactionReversal": lambda n : setattr(self, 'transaction_reversal', n.get_int_value()),
            "transactionType": lambda n : setattr(self, 'transaction_type', n.get_str_value()),
            "transactionTypeCode": lambda n : setattr(self, 'transaction_type_code', n.get_str_value()),
            "valueDate": lambda n : setattr(self, 'value_date', n.get_datetime_value()),
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
        writer.write_float_value("amount", self.amount)
        writer.write_str_value("balanceType", self.balance_type)
        writer.write_str_value("bankRef", self.bank_ref)
        writer.write_int_value("batchNumber", self.batch_number)
        writer.write_str_value("contractNo", self.contract_no)
        writer.write_str_value("currency", self.currency)
        writer.write_float_value("decrease", self.decrease)
        writer.write_str_value("description", self.description)
        writer.write_int_value("direction", self.direction)
        writer.write_float_value("increase", self.increase)
        writer.write_str_value("processTypeCode", self.process_type_code)
        writer.write_str_value("status", self.status)
        writer.write_str_value("statusType", self.status_type)
        writer.write_str_value("statusTypeCode", self.status_type_code)
        writer.write_int_value("transactionAutocode", self.transaction_autocode)
        writer.write_int_value("transactionReversal", self.transaction_reversal)
        writer.write_str_value("transactionType", self.transaction_type)
        writer.write_str_value("transactionTypeCode", self.transaction_type_code)
        writer.write_datetime_value("valueDate", self.value_date)
    

