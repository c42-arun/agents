from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsEquipment(Parsable):
    # The code property
    code: Optional[str] = None
    # The numberOfYearsTrading property
    number_of_years_trading: Optional[int] = None
    # The supplier property
    supplier: Optional[str] = None
    # The supplierReviewDate property
    supplier_review_date: Optional[datetime.datetime] = None
    # The supplierStatus property
    supplier_status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsEquipment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsEquipment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsEquipment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "numberOfYearsTrading": lambda n : setattr(self, 'number_of_years_trading', n.get_int_value()),
            "supplier": lambda n : setattr(self, 'supplier', n.get_str_value()),
            "supplierReviewDate": lambda n : setattr(self, 'supplier_review_date', n.get_datetime_value()),
            "supplierStatus": lambda n : setattr(self, 'supplier_status', n.get_str_value()),
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
        writer.write_str_value("code", self.code)
        writer.write_int_value("numberOfYearsTrading", self.number_of_years_trading)
        writer.write_str_value("supplier", self.supplier)
        writer.write_datetime_value("supplierReviewDate", self.supplier_review_date)
        writer.write_str_value("supplierStatus", self.supplier_status)
    

