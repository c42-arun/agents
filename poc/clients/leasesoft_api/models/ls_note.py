from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsNote(Parsable):
    # The noteText property
    note_text: Optional[str] = None
    # The noteType property
    note_type: Optional[str] = None
    # The userName property
    user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsNote:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsNote
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsNote()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "noteText": lambda n : setattr(self, 'note_text', n.get_str_value()),
            "noteType": lambda n : setattr(self, 'note_type', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
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
        writer.write_str_value("noteText", self.note_text)
        writer.write_str_value("noteType", self.note_type)
        writer.write_str_value("userName", self.user_name)
    

