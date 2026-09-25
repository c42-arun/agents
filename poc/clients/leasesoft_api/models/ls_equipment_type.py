from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsEquipmentType(Parsable):
    # The description property
    description: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The isSoftAsset property
    is_soft_asset: Optional[bool] = None
    # The isVehicle property
    is_vehicle: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsEquipmentType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsEquipmentType
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsEquipmentType()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isSoftAsset": lambda n : setattr(self, 'is_soft_asset', n.get_bool_value()),
            "isVehicle": lambda n : setattr(self, 'is_vehicle', n.get_bool_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isSoftAsset", self.is_soft_asset)
        writer.write_bool_value("isVehicle", self.is_vehicle)
    

