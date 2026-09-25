from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsShortNamesWithAgreements(Parsable):
    # The agreementNo property
    agreement_no: Optional[str] = None
    # The companyName property
    company_name: Optional[str] = None
    # The schema property
    schema: Optional[str] = None
    # The setLiveDate property
    set_live_date: Optional[datetime.datetime] = None
    # The shortName property
    short_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsShortNamesWithAgreements:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsShortNamesWithAgreements
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsShortNamesWithAgreements()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "agreementNo": lambda n : setattr(self, 'agreement_no', n.get_str_value()),
            "companyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "schema": lambda n : setattr(self, 'schema', n.get_str_value()),
            "setLiveDate": lambda n : setattr(self, 'set_live_date', n.get_datetime_value()),
            "shortName": lambda n : setattr(self, 'short_name', n.get_str_value()),
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
        writer.write_str_value("companyName", self.company_name)
        writer.write_str_value("schema", self.schema)
        writer.write_datetime_value("setLiveDate", self.set_live_date)
        writer.write_str_value("shortName", self.short_name)
    

