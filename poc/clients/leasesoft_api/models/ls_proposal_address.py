from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsProposalAddress(Parsable):
    # The atAddressSince property
    at_address_since: Optional[datetime.datetime] = None
    # The flatNo property
    flat_no: Optional[str] = None
    # The houseNo property
    house_no: Optional[str] = None
    # The line1 property
    line1: Optional[str] = None
    # The line2 property
    line2: Optional[str] = None
    # The line3 property
    line3: Optional[str] = None
    # The line4 property
    line4: Optional[str] = None
    # The postcode property
    postcode: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsProposalAddress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsProposalAddress
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsProposalAddress()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "atAddressSince": lambda n : setattr(self, 'at_address_since', n.get_datetime_value()),
            "flatNo": lambda n : setattr(self, 'flat_no', n.get_str_value()),
            "houseNo": lambda n : setattr(self, 'house_no', n.get_str_value()),
            "line1": lambda n : setattr(self, 'line1', n.get_str_value()),
            "line2": lambda n : setattr(self, 'line2', n.get_str_value()),
            "line3": lambda n : setattr(self, 'line3', n.get_str_value()),
            "line4": lambda n : setattr(self, 'line4', n.get_str_value()),
            "postcode": lambda n : setattr(self, 'postcode', n.get_str_value()),
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
        writer.write_datetime_value("atAddressSince", self.at_address_since)
        writer.write_str_value("flatNo", self.flat_no)
        writer.write_str_value("houseNo", self.house_no)
        writer.write_str_value("line1", self.line1)
        writer.write_str_value("line2", self.line2)
        writer.write_str_value("line3", self.line3)
        writer.write_str_value("line4", self.line4)
        writer.write_str_value("postcode", self.postcode)
    

