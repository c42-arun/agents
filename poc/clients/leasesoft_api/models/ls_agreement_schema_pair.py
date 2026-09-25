from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ls_business_line import LsBusinessLine

@dataclass
class LsAgreementSchemaPair(Parsable):
    # The agreementNo property
    agreement_no: Optional[str] = None
    # The allowActions property
    allow_actions: Optional[bool] = None
    # The businessLine property
    business_line: Optional[LsBusinessLine] = None
    # The isBlockDiscount property
    is_block_discount: Optional[bool] = None
    # The isEnded property
    is_ended: Optional[bool] = None
    # The isSupported property
    is_supported: Optional[bool] = None
    # The schema property
    schema: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsAgreementSchemaPair:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsAgreementSchemaPair
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsAgreementSchemaPair()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ls_business_line import LsBusinessLine

        from .ls_business_line import LsBusinessLine

        fields: dict[str, Callable[[Any], None]] = {
            "agreementNo": lambda n : setattr(self, 'agreement_no', n.get_str_value()),
            "allowActions": lambda n : setattr(self, 'allow_actions', n.get_bool_value()),
            "businessLine": lambda n : setattr(self, 'business_line', n.get_enum_value(LsBusinessLine)),
            "isBlockDiscount": lambda n : setattr(self, 'is_block_discount', n.get_bool_value()),
            "isEnded": lambda n : setattr(self, 'is_ended', n.get_bool_value()),
            "isSupported": lambda n : setattr(self, 'is_supported', n.get_bool_value()),
            "schema": lambda n : setattr(self, 'schema', n.get_str_value()),
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
        writer.write_bool_value("allowActions", self.allow_actions)
        writer.write_enum_value("businessLine", self.business_line)
        writer.write_bool_value("isBlockDiscount", self.is_block_discount)
        writer.write_bool_value("isEnded", self.is_ended)
        writer.write_bool_value("isSupported", self.is_supported)
        writer.write_str_value("schema", self.schema)
    

