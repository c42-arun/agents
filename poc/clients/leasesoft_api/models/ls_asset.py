from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ls_address import LsAddress

@dataclass
class LsAsset(Parsable):
    # The assetRegSerialNum property
    asset_reg_serial_num: Optional[str] = None
    # The location property
    location: Optional[LsAddress] = None
    # The name property
    name: Optional[str] = None
    # The otherId property
    other_id: Optional[float] = None
    # The price property
    price: Optional[float] = None
    # The registrationNo property
    registration_no: Optional[str] = None
    # The serialNo property
    serial_no: Optional[str] = None
    # The supplierName property
    supplier_name: Optional[str] = None
    # The supplierShortName property
    supplier_short_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsAsset:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsAsset
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsAsset()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ls_address import LsAddress

        from .ls_address import LsAddress

        fields: dict[str, Callable[[Any], None]] = {
            "assetRegSerialNum": lambda n : setattr(self, 'asset_reg_serial_num', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(LsAddress)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "otherId": lambda n : setattr(self, 'other_id', n.get_float_value()),
            "price": lambda n : setattr(self, 'price', n.get_float_value()),
            "registrationNo": lambda n : setattr(self, 'registration_no', n.get_str_value()),
            "serialNo": lambda n : setattr(self, 'serial_no', n.get_str_value()),
            "supplierName": lambda n : setattr(self, 'supplier_name', n.get_str_value()),
            "supplierShortName": lambda n : setattr(self, 'supplier_short_name', n.get_str_value()),
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
        writer.write_object_value("location", self.location)
        writer.write_str_value("name", self.name)
        writer.write_float_value("otherId", self.other_id)
        writer.write_float_value("price", self.price)
        writer.write_str_value("registrationNo", self.registration_no)
        writer.write_str_value("serialNo", self.serial_no)
        writer.write_str_value("supplierName", self.supplier_name)
        writer.write_str_value("supplierShortName", self.supplier_short_name)
    

