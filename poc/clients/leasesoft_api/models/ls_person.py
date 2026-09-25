from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ls_proposal_address import LsProposalAddress

@dataclass
class LsPerson(Parsable):
    # The address property
    address: Optional[LsProposalAddress] = None
    # The dateOfBirth property
    date_of_birth: Optional[datetime.datetime] = None
    # The email property
    email: Optional[str] = None
    # The facsimile property
    facsimile: Optional[str] = None
    # The forename property
    forename: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The surname property
    surname: Optional[str] = None
    # The telephone property
    telephone: Optional[str] = None
    # The title property
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsPerson:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsPerson
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsPerson()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ls_proposal_address import LsProposalAddress

        from .ls_proposal_address import LsProposalAddress

        fields: dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(LsProposalAddress)),
            "dateOfBirth": lambda n : setattr(self, 'date_of_birth', n.get_datetime_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "facsimile": lambda n : setattr(self, 'facsimile', n.get_str_value()),
            "forename": lambda n : setattr(self, 'forename', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
            "telephone": lambda n : setattr(self, 'telephone', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_object_value("address", self.address)
        writer.write_datetime_value("dateOfBirth", self.date_of_birth)
        writer.write_str_value("email", self.email)
        writer.write_str_value("facsimile", self.facsimile)
        writer.write_str_value("forename", self.forename)
        writer.write_str_value("id", self.id)
        writer.write_str_value("surname", self.surname)
        writer.write_str_value("telephone", self.telephone)
        writer.write_str_value("title", self.title)
    

