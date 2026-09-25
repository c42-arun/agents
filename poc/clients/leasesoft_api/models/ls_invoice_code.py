from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsInvoiceCode(Parsable):
    # The autoCode property
    auto_code: Optional[float] = None
    # The runAutoCode property
    run_auto_code: Optional[float] = None
    # The schema property
    schema: Optional[str] = None
    # The state property
    state: Optional[str] = None
    # The type property
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsInvoiceCode:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsInvoiceCode
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsInvoiceCode()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "autoCode": lambda n : setattr(self, 'auto_code', n.get_float_value()),
            "runAutoCode": lambda n : setattr(self, 'run_auto_code', n.get_float_value()),
            "schema": lambda n : setattr(self, 'schema', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_float_value("autoCode", self.auto_code)
        writer.write_float_value("runAutoCode", self.run_auto_code)
        writer.write_str_value("schema", self.schema)
        writer.write_str_value("state", self.state)
        writer.write_str_value("type", self.type)
    

