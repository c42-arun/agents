from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsShortNameSearchServiceResponse(Parsable):
    # The goldenRecordId property
    golden_record_id: Optional[str] = None
    # The responseMessage property
    response_message: Optional[str] = None
    # The success property
    success: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsShortNameSearchServiceResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsShortNameSearchServiceResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsShortNameSearchServiceResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "goldenRecordId": lambda n : setattr(self, 'golden_record_id', n.get_str_value()),
            "responseMessage": lambda n : setattr(self, 'response_message', n.get_str_value()),
            "success": lambda n : setattr(self, 'success', n.get_bool_value()),
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
        writer.write_str_value("goldenRecordId", self.golden_record_id)
        writer.write_str_value("responseMessage", self.response_message)
        writer.write_bool_value("success", self.success)
    

