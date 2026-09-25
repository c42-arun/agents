from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ls_document import LsDocument

@dataclass
class LsAgreementDocument(Parsable):
    # The agreementNumber property
    agreement_number: Optional[str] = None
    # The document property
    document: Optional[LsDocument] = None
    # The partyShortCode property
    party_short_code: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsAgreementDocument:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsAgreementDocument
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsAgreementDocument()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ls_document import LsDocument

        from .ls_document import LsDocument

        fields: dict[str, Callable[[Any], None]] = {
            "agreementNumber": lambda n : setattr(self, 'agreement_number', n.get_str_value()),
            "document": lambda n : setattr(self, 'document', n.get_object_value(LsDocument)),
            "partyShortCode": lambda n : setattr(self, 'party_short_code', n.get_str_value()),
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
        writer.write_object_value("document", self.document)
        writer.write_str_value("partyShortCode", self.party_short_code)
    

