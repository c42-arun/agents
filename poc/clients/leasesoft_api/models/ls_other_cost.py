from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsOtherCost(Parsable):
    # The contractNo property
    contract_no: Optional[str] = None
    # The costType property
    cost_type: Optional[str] = None
    # The costTypeCode property
    cost_type_code: Optional[str] = None
    # The financed property
    financed: Optional[int] = None
    # The otherCostAmount property
    other_cost_amount: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsOtherCost:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsOtherCost
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsOtherCost()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "contractNo": lambda n : setattr(self, 'contract_no', n.get_str_value()),
            "costType": lambda n : setattr(self, 'cost_type', n.get_str_value()),
            "costTypeCode": lambda n : setattr(self, 'cost_type_code', n.get_str_value()),
            "financed": lambda n : setattr(self, 'financed', n.get_int_value()),
            "otherCostAmount": lambda n : setattr(self, 'other_cost_amount', n.get_float_value()),
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
        writer.write_str_value("contractNo", self.contract_no)
        writer.write_str_value("costType", self.cost_type)
        writer.write_str_value("costTypeCode", self.cost_type_code)
        writer.write_int_value("financed", self.financed)
        writer.write_float_value("otherCostAmount", self.other_cost_amount)
    

