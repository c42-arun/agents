from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsFinancialProfile(Parsable):
    # The amount property
    amount: Optional[float] = None
    # The creditOrDebit property
    credit_or_debit: Optional[int] = None
    # The frequency property
    frequency: Optional[str] = None
    # The numberOf property
    number_of: Optional[int] = None
    # The paymentMethodCode property
    payment_method_code: Optional[str] = None
    # The periodCode property
    period_code: Optional[str] = None
    # The profileAutoCode property
    profile_auto_code: Optional[int] = None
    # The profileType property
    profile_type: Optional[str] = None
    # The profileTypeCode property
    profile_type_code: Optional[str] = None
    # The startDate property
    start_date: Optional[datetime.datetime] = None
    # The vatCode property
    vat_code: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsFinancialProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsFinancialProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsFinancialProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "amount": lambda n : setattr(self, 'amount', n.get_float_value()),
            "creditOrDebit": lambda n : setattr(self, 'credit_or_debit', n.get_int_value()),
            "frequency": lambda n : setattr(self, 'frequency', n.get_str_value()),
            "numberOf": lambda n : setattr(self, 'number_of', n.get_int_value()),
            "paymentMethodCode": lambda n : setattr(self, 'payment_method_code', n.get_str_value()),
            "periodCode": lambda n : setattr(self, 'period_code', n.get_str_value()),
            "profileAutoCode": lambda n : setattr(self, 'profile_auto_code', n.get_int_value()),
            "profileType": lambda n : setattr(self, 'profile_type', n.get_str_value()),
            "profileTypeCode": lambda n : setattr(self, 'profile_type_code', n.get_str_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_datetime_value()),
            "vatCode": lambda n : setattr(self, 'vat_code', n.get_str_value()),
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
        writer.write_int_value("creditOrDebit", self.credit_or_debit)
        writer.write_str_value("frequency", self.frequency)
        writer.write_int_value("numberOf", self.number_of)
        writer.write_str_value("paymentMethodCode", self.payment_method_code)
        writer.write_str_value("periodCode", self.period_code)
        writer.write_int_value("profileAutoCode", self.profile_auto_code)
        writer.write_str_value("profileType", self.profile_type)
        writer.write_str_value("profileTypeCode", self.profile_type_code)
        writer.write_datetime_value("startDate", self.start_date)
        writer.write_str_value("vatCode", self.vat_code)
    

