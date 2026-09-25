from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsAgreementNote(Parsable):
    # The actionUserId property
    action_user_id: Optional[str] = None
    # The agreementReviewDate property
    agreement_review_date: Optional[datetime.datetime] = None
    # The author property
    author: Optional[str] = None
    # The diarisedForGroup property
    diarised_for_group: Optional[str] = None
    # The diarisedForGroupCode property
    diarised_for_group_code: Optional[str] = None
    # The diarisedForUser property
    diarised_for_user: Optional[str] = None
    # The diaryTaskStatus property
    diary_task_status: Optional[int] = None
    # The entryDate property
    entry_date: Optional[datetime.datetime] = None
    # The entryType property
    entry_type: Optional[str] = None
    # The eventDate property
    event_date: Optional[datetime.datetime] = None
    # The noteLevel property
    note_level: Optional[str] = None
    # The noteText property
    note_text: Optional[str] = None
    # The noteTypeCode property
    note_type_code: Optional[str] = None
    # The noteTypeCodeDescription property
    note_type_code_description: Optional[str] = None
    # The notesAutoCode property
    notes_auto_code: Optional[int] = None
    # The opUserId property
    op_user_id: Optional[str] = None
    # The reviewDate property
    review_date: Optional[datetime.datetime] = None
    # The systemNote property
    system_note: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsAgreementNote:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsAgreementNote
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsAgreementNote()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "actionUserId": lambda n : setattr(self, 'action_user_id', n.get_str_value()),
            "agreementReviewDate": lambda n : setattr(self, 'agreement_review_date', n.get_datetime_value()),
            "author": lambda n : setattr(self, 'author', n.get_str_value()),
            "diarisedForGroup": lambda n : setattr(self, 'diarised_for_group', n.get_str_value()),
            "diarisedForGroupCode": lambda n : setattr(self, 'diarised_for_group_code', n.get_str_value()),
            "diarisedForUser": lambda n : setattr(self, 'diarised_for_user', n.get_str_value()),
            "diaryTaskStatus": lambda n : setattr(self, 'diary_task_status', n.get_int_value()),
            "entryDate": lambda n : setattr(self, 'entry_date', n.get_datetime_value()),
            "entryType": lambda n : setattr(self, 'entry_type', n.get_str_value()),
            "eventDate": lambda n : setattr(self, 'event_date', n.get_datetime_value()),
            "noteLevel": lambda n : setattr(self, 'note_level', n.get_str_value()),
            "noteText": lambda n : setattr(self, 'note_text', n.get_str_value()),
            "noteTypeCode": lambda n : setattr(self, 'note_type_code', n.get_str_value()),
            "noteTypeCodeDescription": lambda n : setattr(self, 'note_type_code_description', n.get_str_value()),
            "notesAutoCode": lambda n : setattr(self, 'notes_auto_code', n.get_int_value()),
            "opUserId": lambda n : setattr(self, 'op_user_id', n.get_str_value()),
            "reviewDate": lambda n : setattr(self, 'review_date', n.get_datetime_value()),
            "systemNote": lambda n : setattr(self, 'system_note', n.get_int_value()),
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
        writer.write_str_value("actionUserId", self.action_user_id)
        writer.write_datetime_value("agreementReviewDate", self.agreement_review_date)
        writer.write_str_value("author", self.author)
        writer.write_str_value("diarisedForGroup", self.diarised_for_group)
        writer.write_str_value("diarisedForGroupCode", self.diarised_for_group_code)
        writer.write_str_value("diarisedForUser", self.diarised_for_user)
        writer.write_int_value("diaryTaskStatus", self.diary_task_status)
        writer.write_datetime_value("entryDate", self.entry_date)
        writer.write_str_value("entryType", self.entry_type)
        writer.write_datetime_value("eventDate", self.event_date)
        writer.write_str_value("noteLevel", self.note_level)
        writer.write_str_value("noteText", self.note_text)
        writer.write_str_value("noteTypeCode", self.note_type_code)
        writer.write_str_value("noteTypeCodeDescription", self.note_type_code_description)
        writer.write_int_value("notesAutoCode", self.notes_auto_code)
        writer.write_str_value("opUserId", self.op_user_id)
        writer.write_datetime_value("reviewDate", self.review_date)
        writer.write_int_value("systemNote", self.system_note)
    

