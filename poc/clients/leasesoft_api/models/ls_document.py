from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsDocument(Parsable):
    # The description property
    description: Optional[str] = None
    # The dipRecord property
    dip_record: Optional[float] = None
    # The documentType property
    document_type: Optional[str] = None
    # The fileExtension property
    file_extension: Optional[str] = None
    # The filename property
    filename: Optional[str] = None
    # The indexDate property
    index_date: Optional[datetime.datetime] = None
    # The note property
    note: Optional[str] = None
    # The reference property
    reference: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsDocument:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsDocument
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsDocument()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "dipRecord": lambda n : setattr(self, 'dip_record', n.get_float_value()),
            "documentType": lambda n : setattr(self, 'document_type', n.get_str_value()),
            "fileExtension": lambda n : setattr(self, 'file_extension', n.get_str_value()),
            "filename": lambda n : setattr(self, 'filename', n.get_str_value()),
            "indexDate": lambda n : setattr(self, 'index_date', n.get_datetime_value()),
            "note": lambda n : setattr(self, 'note', n.get_str_value()),
            "reference": lambda n : setattr(self, 'reference', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_float_value("dipRecord", self.dip_record)
        writer.write_str_value("documentType", self.document_type)
        writer.write_str_value("fileExtension", self.file_extension)
        writer.write_str_value("filename", self.filename)
        writer.write_datetime_value("indexDate", self.index_date)
        writer.write_str_value("note", self.note)
        writer.write_str_value("reference", self.reference)
    

