from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsTransaction(Parsable):
    # The currencyCode property
    currency_code: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The feeAmount property
    fee_amount: Optional[float] = None
    # The insurancePremium property
    insurance_premium: Optional[float] = None
    # The maintenanceCharge property
    maintenance_charge: Optional[float] = None
    # The paymentDue property
    payment_due: Optional[float] = None
    # The paymentMade property
    payment_made: Optional[float] = None
    # The repaymentsDue property
    repayments_due: Optional[float] = None
    # The transTypeGroup property
    trans_type_group: Optional[int] = None
    # The transactionDate property
    transaction_date: Optional[datetime.datetime] = None
    # The vat property
    vat: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsTransaction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsTransaction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsTransaction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "currencyCode": lambda n : setattr(self, 'currency_code', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "feeAmount": lambda n : setattr(self, 'fee_amount', n.get_float_value()),
            "insurancePremium": lambda n : setattr(self, 'insurance_premium', n.get_float_value()),
            "maintenanceCharge": lambda n : setattr(self, 'maintenance_charge', n.get_float_value()),
            "paymentDue": lambda n : setattr(self, 'payment_due', n.get_float_value()),
            "paymentMade": lambda n : setattr(self, 'payment_made', n.get_float_value()),
            "repaymentsDue": lambda n : setattr(self, 'repayments_due', n.get_float_value()),
            "transTypeGroup": lambda n : setattr(self, 'trans_type_group', n.get_int_value()),
            "transactionDate": lambda n : setattr(self, 'transaction_date', n.get_datetime_value()),
            "vat": lambda n : setattr(self, 'vat', n.get_float_value()),
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
        writer.write_str_value("currencyCode", self.currency_code)
        writer.write_str_value("description", self.description)
        writer.write_float_value("feeAmount", self.fee_amount)
        writer.write_float_value("insurancePremium", self.insurance_premium)
        writer.write_float_value("maintenanceCharge", self.maintenance_charge)
        writer.write_float_value("paymentDue", self.payment_due)
        writer.write_float_value("paymentMade", self.payment_made)
        writer.write_float_value("repaymentsDue", self.repayments_due)
        writer.write_int_value("transTypeGroup", self.trans_type_group)
        writer.write_datetime_value("transactionDate", self.transaction_date)
        writer.write_float_value("vat", self.vat)
    

