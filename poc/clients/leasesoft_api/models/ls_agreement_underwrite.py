from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsAgreementUnderwrite(Parsable):
    # The creditAutoCode property
    credit_auto_code: Optional[int] = None
    # The lastCreditDate property
    last_credit_date: Optional[datetime.datetime] = None
    # The proposalNumber property
    proposal_number: Optional[str] = None
    # The statusCode property
    status_code: Optional[str] = None
    # The subStatusCode property
    sub_status_code: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsAgreementUnderwrite:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsAgreementUnderwrite
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsAgreementUnderwrite()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "creditAutoCode": lambda n : setattr(self, 'credit_auto_code', n.get_int_value()),
            "lastCreditDate": lambda n : setattr(self, 'last_credit_date', n.get_datetime_value()),
            "proposalNumber": lambda n : setattr(self, 'proposal_number', n.get_str_value()),
            "statusCode": lambda n : setattr(self, 'status_code', n.get_str_value()),
            "subStatusCode": lambda n : setattr(self, 'sub_status_code', n.get_str_value()),
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
        writer.write_int_value("creditAutoCode", self.credit_auto_code)
        writer.write_datetime_value("lastCreditDate", self.last_credit_date)
        writer.write_str_value("proposalNumber", self.proposal_number)
        writer.write_str_value("statusCode", self.status_code)
        writer.write_str_value("subStatusCode", self.sub_status_code)
    

