from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ls_asset_supplier import LsAssetSupplier
    from .ls_asset_type import LsAssetType
    from .ls_hard_or_soft_asset import LsHardOrSoftAsset

@dataclass
class LsAssetDetails(Parsable):
    # The assetAutoCode property
    asset_auto_code: Optional[int] = None
    # The assetCashPrice property
    asset_cash_price: Optional[float] = None
    # The assetDescription property
    asset_description: Optional[str] = None
    # The assetDetailAutoCode property
    asset_detail_auto_code: Optional[int] = None
    # The assetEquipmentCode property
    asset_equipment_code: Optional[str] = None
    # The assetResidualValue property
    asset_residual_value: Optional[float] = None
    # The assetType property
    asset_type: Optional[LsAssetType] = None
    # The assetTypeCode property
    asset_type_code: Optional[int] = None
    # The capId property
    cap_id: Optional[str] = None
    # The cashPrice property
    cash_price: Optional[float] = None
    # The chassisSerialNo property
    chassis_serial_no: Optional[str] = None
    # The count property
    count: Optional[int] = None
    # The description property
    description: Optional[str] = None
    # The equipmentType property
    equipment_type: Optional[str] = None
    # The externalVariantId property
    external_variant_id: Optional[str] = None
    # The externalVariantIdProvider property
    external_variant_id_provider: Optional[str] = None
    # The hardOrSoftAsset property
    hard_or_soft_asset: Optional[LsHardOrSoftAsset] = None
    # The make property
    make: Optional[str] = None
    # The memo property
    memo: Optional[str] = None
    # The model property
    model: Optional[str] = None
    # The newOrUsed property
    new_or_used: Optional[int] = None
    # The otherIdNumber property
    other_id_number: Optional[str] = None
    # The recordedMileage property
    recorded_mileage: Optional[str] = None
    # The regNo property
    reg_no: Optional[str] = None
    # The residualValue property
    residual_value: Optional[float] = None
    # The rvAmount property
    rv_amount: Optional[float] = None
    # The supplier property
    supplier: Optional[LsAssetSupplier] = None
    # The trim property
    trim: Optional[str] = None
    # The vatQualifying property
    vat_qualifying: Optional[int] = None
    # The vin property
    vin: Optional[str] = None
    # The yearOfManufacture property
    year_of_manufacture: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsAssetDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsAssetDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsAssetDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ls_asset_supplier import LsAssetSupplier
        from .ls_asset_type import LsAssetType
        from .ls_hard_or_soft_asset import LsHardOrSoftAsset

        from .ls_asset_supplier import LsAssetSupplier
        from .ls_asset_type import LsAssetType
        from .ls_hard_or_soft_asset import LsHardOrSoftAsset

        fields: dict[str, Callable[[Any], None]] = {
            "assetAutoCode": lambda n : setattr(self, 'asset_auto_code', n.get_int_value()),
            "assetCashPrice": lambda n : setattr(self, 'asset_cash_price', n.get_float_value()),
            "assetDescription": lambda n : setattr(self, 'asset_description', n.get_str_value()),
            "assetDetailAutoCode": lambda n : setattr(self, 'asset_detail_auto_code', n.get_int_value()),
            "assetEquipmentCode": lambda n : setattr(self, 'asset_equipment_code', n.get_str_value()),
            "assetResidualValue": lambda n : setattr(self, 'asset_residual_value', n.get_float_value()),
            "assetType": lambda n : setattr(self, 'asset_type', n.get_enum_value(LsAssetType)),
            "assetTypeCode": lambda n : setattr(self, 'asset_type_code', n.get_int_value()),
            "capId": lambda n : setattr(self, 'cap_id', n.get_str_value()),
            "cashPrice": lambda n : setattr(self, 'cash_price', n.get_float_value()),
            "chassisSerialNo": lambda n : setattr(self, 'chassis_serial_no', n.get_str_value()),
            "count": lambda n : setattr(self, 'count', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "equipmentType": lambda n : setattr(self, 'equipment_type', n.get_str_value()),
            "externalVariantId": lambda n : setattr(self, 'external_variant_id', n.get_str_value()),
            "externalVariantIdProvider": lambda n : setattr(self, 'external_variant_id_provider', n.get_str_value()),
            "hardOrSoftAsset": lambda n : setattr(self, 'hard_or_soft_asset', n.get_enum_value(LsHardOrSoftAsset)),
            "make": lambda n : setattr(self, 'make', n.get_str_value()),
            "memo": lambda n : setattr(self, 'memo', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "newOrUsed": lambda n : setattr(self, 'new_or_used', n.get_int_value()),
            "otherIdNumber": lambda n : setattr(self, 'other_id_number', n.get_str_value()),
            "recordedMileage": lambda n : setattr(self, 'recorded_mileage', n.get_str_value()),
            "regNo": lambda n : setattr(self, 'reg_no', n.get_str_value()),
            "residualValue": lambda n : setattr(self, 'residual_value', n.get_float_value()),
            "rvAmount": lambda n : setattr(self, 'rv_amount', n.get_float_value()),
            "supplier": lambda n : setattr(self, 'supplier', n.get_object_value(LsAssetSupplier)),
            "trim": lambda n : setattr(self, 'trim', n.get_str_value()),
            "vatQualifying": lambda n : setattr(self, 'vat_qualifying', n.get_int_value()),
            "vin": lambda n : setattr(self, 'vin', n.get_str_value()),
            "yearOfManufacture": lambda n : setattr(self, 'year_of_manufacture', n.get_datetime_value()),
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
        writer.write_int_value("assetAutoCode", self.asset_auto_code)
        writer.write_float_value("assetCashPrice", self.asset_cash_price)
        writer.write_str_value("assetDescription", self.asset_description)
        writer.write_int_value("assetDetailAutoCode", self.asset_detail_auto_code)
        writer.write_str_value("assetEquipmentCode", self.asset_equipment_code)
        writer.write_float_value("assetResidualValue", self.asset_residual_value)
        writer.write_enum_value("assetType", self.asset_type)
        writer.write_int_value("assetTypeCode", self.asset_type_code)
        writer.write_str_value("capId", self.cap_id)
        writer.write_float_value("cashPrice", self.cash_price)
        writer.write_str_value("chassisSerialNo", self.chassis_serial_no)
        writer.write_int_value("count", self.count)
        writer.write_str_value("description", self.description)
        writer.write_str_value("equipmentType", self.equipment_type)
        writer.write_str_value("externalVariantId", self.external_variant_id)
        writer.write_str_value("externalVariantIdProvider", self.external_variant_id_provider)
        writer.write_enum_value("hardOrSoftAsset", self.hard_or_soft_asset)
        writer.write_str_value("make", self.make)
        writer.write_str_value("memo", self.memo)
        writer.write_str_value("model", self.model)
        writer.write_int_value("newOrUsed", self.new_or_used)
        writer.write_str_value("otherIdNumber", self.other_id_number)
        writer.write_str_value("recordedMileage", self.recorded_mileage)
        writer.write_str_value("regNo", self.reg_no)
        writer.write_float_value("residualValue", self.residual_value)
        writer.write_float_value("rvAmount", self.rv_amount)
        writer.write_object_value("supplier", self.supplier)
        writer.write_str_value("trim", self.trim)
        writer.write_int_value("vatQualifying", self.vat_qualifying)
        writer.write_str_value("vin", self.vin)
        writer.write_datetime_value("yearOfManufacture", self.year_of_manufacture)
    

