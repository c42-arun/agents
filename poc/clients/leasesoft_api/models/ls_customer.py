from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsCustomer(Parsable):
    # The addressLine1 property
    address_line1: Optional[str] = None
    # The addressLine2 property
    address_line2: Optional[str] = None
    # The addressLine3 property
    address_line3: Optional[str] = None
    # The addressLine4 property
    address_line4: Optional[str] = None
    # The firstName property
    first_name: Optional[str] = None
    # The postCode property
    post_code: Optional[str] = None
    # The schema property
    schema: Optional[str] = None
    # The shortName property
    short_name: Optional[str] = None
    # The surnameCompanyName property
    surname_company_name: Optional[str] = None
    # The tradingAs property
    trading_as: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsCustomer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsCustomer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsCustomer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "addressLine1": lambda n : setattr(self, 'address_line1', n.get_str_value()),
            "addressLine2": lambda n : setattr(self, 'address_line2', n.get_str_value()),
            "addressLine3": lambda n : setattr(self, 'address_line3', n.get_str_value()),
            "addressLine4": lambda n : setattr(self, 'address_line4', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "postCode": lambda n : setattr(self, 'post_code', n.get_str_value()),
            "schema": lambda n : setattr(self, 'schema', n.get_str_value()),
            "shortName": lambda n : setattr(self, 'short_name', n.get_str_value()),
            "surnameCompanyName": lambda n : setattr(self, 'surname_company_name', n.get_str_value()),
            "tradingAs": lambda n : setattr(self, 'trading_as', n.get_str_value()),
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
        writer.write_str_value("addressLine1", self.address_line1)
        writer.write_str_value("addressLine2", self.address_line2)
        writer.write_str_value("addressLine3", self.address_line3)
        writer.write_str_value("addressLine4", self.address_line4)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("postCode", self.post_code)
        writer.write_str_value("schema", self.schema)
        writer.write_str_value("shortName", self.short_name)
        writer.write_str_value("surnameCompanyName", self.surname_company_name)
        writer.write_str_value("tradingAs", self.trading_as)
    

