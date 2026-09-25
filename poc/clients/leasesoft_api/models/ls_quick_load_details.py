from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsQuickLoadDetails(Parsable):
    # The agreementNumber property
    agreement_number: Optional[str] = None
    # The fullLoadEdit property
    full_load_edit: Optional[int] = None
    # The schema property
    schema: Optional[str] = None
    # The statusCode property
    status_code: Optional[str] = None
    # The statusDescription property
    status_description: Optional[str] = None
    # The subStatusCode property
    sub_status_code: Optional[str] = None
    # The subStatusDescription property
    sub_status_description: Optional[str] = None
    # The useQuickLoad property
    use_quick_load: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsQuickLoadDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsQuickLoadDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsQuickLoadDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "agreementNumber": lambda n : setattr(self, 'agreement_number', n.get_str_value()),
            "fullLoadEdit": lambda n : setattr(self, 'full_load_edit', n.get_int_value()),
            "schema": lambda n : setattr(self, 'schema', n.get_str_value()),
            "statusCode": lambda n : setattr(self, 'status_code', n.get_str_value()),
            "statusDescription": lambda n : setattr(self, 'status_description', n.get_str_value()),
            "subStatusCode": lambda n : setattr(self, 'sub_status_code', n.get_str_value()),
            "subStatusDescription": lambda n : setattr(self, 'sub_status_description', n.get_str_value()),
            "useQuickLoad": lambda n : setattr(self, 'use_quick_load', n.get_int_value()),
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
        writer.write_int_value("fullLoadEdit", self.full_load_edit)
        writer.write_str_value("schema", self.schema)
        writer.write_str_value("statusCode", self.status_code)
        writer.write_str_value("statusDescription", self.status_description)
        writer.write_str_value("subStatusCode", self.sub_status_code)
        writer.write_str_value("subStatusDescription", self.sub_status_description)
        writer.write_int_value("useQuickLoad", self.use_quick_load)
    

