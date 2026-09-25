from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsDocumentCollateral(Parsable):
    # The assetDetailAutocode property
    asset_detail_autocode: Optional[int] = None
    # The clientName property
    client_name: Optional[str] = None
    # The contractNo property
    contract_no: Optional[str] = None
    # The date property
    date: Optional[datetime.datetime] = None
    # The dipAutocode property
    dip_autocode: Optional[int] = None
    # The documentRef property
    document_ref: Optional[str] = None
    # The documentType property
    document_type: Optional[str] = None
    # The documentTypeCode property
    document_type_code: Optional[str] = None
    # The duplicate property
    duplicate: Optional[int] = None
    # The fileLocation property
    file_location: Optional[str] = None
    # The groupName property
    group_name: Optional[str] = None
    # The notes property
    notes: Optional[str] = None
    # The partial property
    partial: Optional[int] = None
    # The status property
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsDocumentCollateral:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsDocumentCollateral
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsDocumentCollateral()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "assetDetailAutocode": lambda n : setattr(self, 'asset_detail_autocode', n.get_int_value()),
            "clientName": lambda n : setattr(self, 'client_name', n.get_str_value()),
            "contractNo": lambda n : setattr(self, 'contract_no', n.get_str_value()),
            "date": lambda n : setattr(self, 'date', n.get_datetime_value()),
            "dipAutocode": lambda n : setattr(self, 'dip_autocode', n.get_int_value()),
            "documentRef": lambda n : setattr(self, 'document_ref', n.get_str_value()),
            "documentType": lambda n : setattr(self, 'document_type', n.get_str_value()),
            "documentTypeCode": lambda n : setattr(self, 'document_type_code', n.get_str_value()),
            "duplicate": lambda n : setattr(self, 'duplicate', n.get_int_value()),
            "fileLocation": lambda n : setattr(self, 'file_location', n.get_str_value()),
            "groupName": lambda n : setattr(self, 'group_name', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "partial": lambda n : setattr(self, 'partial', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_int_value("assetDetailAutocode", self.asset_detail_autocode)
        writer.write_str_value("clientName", self.client_name)
        writer.write_str_value("contractNo", self.contract_no)
        writer.write_datetime_value("date", self.date)
        writer.write_int_value("dipAutocode", self.dip_autocode)
        writer.write_str_value("documentRef", self.document_ref)
        writer.write_str_value("documentType", self.document_type)
        writer.write_str_value("documentTypeCode", self.document_type_code)
        writer.write_int_value("duplicate", self.duplicate)
        writer.write_str_value("fileLocation", self.file_location)
        writer.write_str_value("groupName", self.group_name)
        writer.write_str_value("notes", self.notes)
        writer.write_int_value("partial", self.partial)
        writer.write_str_value("status", self.status)
    

