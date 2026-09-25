from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ls_proposal_notes import LsProposalNotes
    from .ls_proposal_status import LsProposalStatus

@dataclass
class LsProposalNotesSummary(Parsable):
    # The agreementNo property
    agreement_no: Optional[str] = None
    # The clientName property
    client_name: Optional[str] = None
    # The contractTypeCode property
    contract_type_code: Optional[str] = None
    # The proposalNotes property
    proposal_notes: Optional[LsProposalNotes] = None
    # The reference property
    reference: Optional[str] = None
    # The schema property
    schema: Optional[str] = None
    # The status property
    status: Optional[LsProposalStatus] = None
    # The updatedDate property
    updated_date: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsProposalNotesSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsProposalNotesSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsProposalNotesSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ls_proposal_notes import LsProposalNotes
        from .ls_proposal_status import LsProposalStatus

        from .ls_proposal_notes import LsProposalNotes
        from .ls_proposal_status import LsProposalStatus

        fields: dict[str, Callable[[Any], None]] = {
            "agreementNo": lambda n : setattr(self, 'agreement_no', n.get_str_value()),
            "clientName": lambda n : setattr(self, 'client_name', n.get_str_value()),
            "contractTypeCode": lambda n : setattr(self, 'contract_type_code', n.get_str_value()),
            "proposalNotes": lambda n : setattr(self, 'proposal_notes', n.get_object_value(LsProposalNotes)),
            "reference": lambda n : setattr(self, 'reference', n.get_str_value()),
            "schema": lambda n : setattr(self, 'schema', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_object_value(LsProposalStatus)),
            "updatedDate": lambda n : setattr(self, 'updated_date', n.get_datetime_value()),
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
        writer.write_str_value("agreementNo", self.agreement_no)
        writer.write_str_value("clientName", self.client_name)
        writer.write_str_value("contractTypeCode", self.contract_type_code)
        writer.write_object_value("proposalNotes", self.proposal_notes)
        writer.write_str_value("reference", self.reference)
        writer.write_str_value("schema", self.schema)
        writer.write_object_value("status", self.status)
        writer.write_datetime_value("updatedDate", self.updated_date)
    

