from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsPrimaryContactDetails(Parsable):
    # The email property
    email: Optional[str] = None
    # The firstName property
    first_name: Optional[str] = None
    # The lastName property
    last_name: Optional[str] = None
    # The mobileNumber property
    mobile_number: Optional[str] = None
    # The position property
    position: Optional[str] = None
    # The typeCode property
    type_code: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsPrimaryContactDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsPrimaryContactDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsPrimaryContactDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "mobileNumber": lambda n : setattr(self, 'mobile_number', n.get_str_value()),
            "position": lambda n : setattr(self, 'position', n.get_str_value()),
            "typeCode": lambda n : setattr(self, 'type_code', n.get_str_value()),
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
        writer.write_str_value("email", self.email)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("lastName", self.last_name)
        writer.write_str_value("mobileNumber", self.mobile_number)
        writer.write_str_value("position", self.position)
        writer.write_str_value("typeCode", self.type_code)
    

