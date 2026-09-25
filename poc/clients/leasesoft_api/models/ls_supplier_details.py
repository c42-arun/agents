from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsSupplierDetails(Parsable):
    # The addressLine1 property
    address_line1: Optional[str] = None
    # The addressLine2 property
    address_line2: Optional[str] = None
    # The approvalStatus property
    approval_status: Optional[str] = None
    # The city property
    city: Optional[str] = None
    # The postCode property
    post_code: Optional[str] = None
    # The requiresApproval property
    requires_approval: Optional[bool] = None
    # The supplierName property
    supplier_name: Optional[str] = None
    # The supplierShortCode property
    supplier_short_code: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsSupplierDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsSupplierDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsSupplierDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "addressLine1": lambda n : setattr(self, 'address_line1', n.get_str_value()),
            "addressLine2": lambda n : setattr(self, 'address_line2', n.get_str_value()),
            "approvalStatus": lambda n : setattr(self, 'approval_status', n.get_str_value()),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "postCode": lambda n : setattr(self, 'post_code', n.get_str_value()),
            "requiresApproval": lambda n : setattr(self, 'requires_approval', n.get_bool_value()),
            "supplierName": lambda n : setattr(self, 'supplier_name', n.get_str_value()),
            "supplierShortCode": lambda n : setattr(self, 'supplier_short_code', n.get_str_value()),
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
        writer.write_str_value("addressLine1", self.address_line1)
        writer.write_str_value("addressLine2", self.address_line2)
        writer.write_str_value("approvalStatus", self.approval_status)
        writer.write_str_value("city", self.city)
        writer.write_str_value("postCode", self.post_code)
        writer.write_bool_value("requiresApproval", self.requires_approval)
        writer.write_str_value("supplierName", self.supplier_name)
        writer.write_str_value("supplierShortCode", self.supplier_short_code)
    

