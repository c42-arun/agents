from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsAssetSupplier(Parsable):
    # The addressLine1 property
    address_line1: Optional[str] = None
    # The addressLine2 property
    address_line2: Optional[str] = None
    # The addressLine3 property
    address_line3: Optional[str] = None
    # The addressLine4 property
    address_line4: Optional[str] = None
    # The approved property
    approved: Optional[int] = None
    # The firstName property
    first_name: Optional[str] = None
    # The flatNo property
    flat_no: Optional[str] = None
    # The houseNo property
    house_no: Optional[str] = None
    # The otherName property
    other_name: Optional[str] = None
    # The postCode property
    post_code: Optional[str] = None
    # The shortName property
    short_name: Optional[str] = None
    # The status property
    status: Optional[str] = None
    # The statusCode property
    status_code: Optional[str] = None
    # The surnameCompany property
    surname_company: Optional[str] = None
    # The tradingAs property
    trading_as: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsAssetSupplier:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsAssetSupplier
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsAssetSupplier()
    
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
            "approved": lambda n : setattr(self, 'approved', n.get_int_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "flatNo": lambda n : setattr(self, 'flat_no', n.get_str_value()),
            "houseNo": lambda n : setattr(self, 'house_no', n.get_str_value()),
            "otherName": lambda n : setattr(self, 'other_name', n.get_str_value()),
            "postCode": lambda n : setattr(self, 'post_code', n.get_str_value()),
            "shortName": lambda n : setattr(self, 'short_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "statusCode": lambda n : setattr(self, 'status_code', n.get_str_value()),
            "surnameCompany": lambda n : setattr(self, 'surname_company', n.get_str_value()),
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
        writer.write_int_value("approved", self.approved)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("flatNo", self.flat_no)
        writer.write_str_value("houseNo", self.house_no)
        writer.write_str_value("otherName", self.other_name)
        writer.write_str_value("postCode", self.post_code)
        writer.write_str_value("shortName", self.short_name)
        writer.write_str_value("status", self.status)
        writer.write_str_value("statusCode", self.status_code)
        writer.write_str_value("surnameCompany", self.surname_company)
        writer.write_str_value("tradingAs", self.trading_as)
    

