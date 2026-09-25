from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsEmailAttachmentInfo(Parsable):
    # The attachmentId property
    attachment_id: Optional[str] = None
    # The canPreviewInline property
    can_preview_inline: Optional[bool] = None
    # The contentType property
    content_type: Optional[str] = None
    # The fileName property
    file_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsEmailAttachmentInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsEmailAttachmentInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsEmailAttachmentInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "attachmentId": lambda n : setattr(self, 'attachment_id', n.get_str_value()),
            "canPreviewInline": lambda n : setattr(self, 'can_preview_inline', n.get_bool_value()),
            "contentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
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
        writer.write_str_value("attachmentId", self.attachment_id)
        writer.write_bool_value("canPreviewInline", self.can_preview_inline)
        writer.write_str_value("contentType", self.content_type)
        writer.write_str_value("fileName", self.file_name)
    

