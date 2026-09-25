from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsInvoice(Parsable):
    # The agreementNumber property
    agreement_number: Optional[str] = None
    # The autoCode property
    auto_code: Optional[float] = None
    # The code property
    code: Optional[str] = None
    # The date property
    date: Optional[datetime.datetime] = None
    # The description property
    description: Optional[str] = None
    # The grossTotal property
    gross_total: Optional[float] = None
    # The invTotal property
    inv_total: Optional[float] = None
    # The number property
    number: Optional[str] = None
    # The shortName property
    short_name: Optional[str] = None
    # The state property
    state: Optional[str] = None
    # The type property
    type: Optional[str] = None
    # The vatExemptTotal property
    vat_exempt_total: Optional[float] = None
    # The vatTotal property
    vat_total: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsInvoice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsInvoice
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsInvoice()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "agreementNumber": lambda n : setattr(self, 'agreement_number', n.get_str_value()),
            "autoCode": lambda n : setattr(self, 'auto_code', n.get_float_value()),
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "date": lambda n : setattr(self, 'date', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "grossTotal": lambda n : setattr(self, 'gross_total', n.get_float_value()),
            "invTotal": lambda n : setattr(self, 'inv_total', n.get_float_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "shortName": lambda n : setattr(self, 'short_name', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "vatExemptTotal": lambda n : setattr(self, 'vat_exempt_total', n.get_float_value()),
            "vatTotal": lambda n : setattr(self, 'vat_total', n.get_float_value()),
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
        writer.write_str_value("agreementNumber", self.agreement_number)
        writer.write_float_value("autoCode", self.auto_code)
        writer.write_str_value("code", self.code)
        writer.write_datetime_value("date", self.date)
        writer.write_str_value("description", self.description)
        writer.write_float_value("grossTotal", self.gross_total)
        writer.write_float_value("invTotal", self.inv_total)
        writer.write_str_value("number", self.number)
        writer.write_str_value("shortName", self.short_name)
        writer.write_str_value("state", self.state)
        writer.write_str_value("type", self.type)
        writer.write_float_value("vatExemptTotal", self.vat_exempt_total)
        writer.write_float_value("vatTotal", self.vat_total)
    

