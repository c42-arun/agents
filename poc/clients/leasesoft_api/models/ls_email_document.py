from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ls_email_attachment_info import LsEmailAttachmentInfo

@dataclass
class LsEmailDocument(Parsable):
    # The attachments property
    attachments: Optional[list[LsEmailAttachmentInfo]] = None
    # The cc property
    cc: Optional[str] = None
    # The from property
    from_: Optional[str] = None
    # The htmlBody property
    html_body: Optional[str] = None
    # The sentDate property
    sent_date: Optional[datetime.datetime] = None
    # The subject property
    subject: Optional[str] = None
    # The textBody property
    text_body: Optional[str] = None
    # The to property
    to: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsEmailDocument:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsEmailDocument
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsEmailDocument()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ls_email_attachment_info import LsEmailAttachmentInfo

        from .ls_email_attachment_info import LsEmailAttachmentInfo

        fields: dict[str, Callable[[Any], None]] = {
            "attachments": lambda n : setattr(self, 'attachments', n.get_collection_of_object_values(LsEmailAttachmentInfo)),
            "cc": lambda n : setattr(self, 'cc', n.get_str_value()),
            "from": lambda n : setattr(self, 'from_', n.get_str_value()),
            "htmlBody": lambda n : setattr(self, 'html_body', n.get_str_value()),
            "sentDate": lambda n : setattr(self, 'sent_date', n.get_datetime_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "textBody": lambda n : setattr(self, 'text_body', n.get_str_value()),
            "to": lambda n : setattr(self, 'to', n.get_str_value()),
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
        writer.write_collection_of_object_values("attachments", self.attachments)
        writer.write_str_value("cc", self.cc)
        writer.write_str_value("from", self.from_)
        writer.write_str_value("htmlBody", self.html_body)
        writer.write_datetime_value("sentDate", self.sent_date)
        writer.write_str_value("subject", self.subject)
        writer.write_str_value("textBody", self.text_body)
        writer.write_str_value("to", self.to)
    

