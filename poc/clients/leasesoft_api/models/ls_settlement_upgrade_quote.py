from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ls_quote_type import LsQuoteType

@dataclass
class LsSettlementUpgradeQuote(Parsable):
    # The arrears property
    arrears: Optional[float] = None
    # The balance property
    balance: Optional[float] = None
    # The discount property
    discount: Optional[float] = None
    # The netSettlement property
    net_settlement: Optional[float] = None
    # The quoteType property
    quote_type: Optional[LsQuoteType] = None
    # The settlementFee property
    settlement_fee: Optional[float] = None
    # The total property
    total: Optional[float] = None
    # The validTo property
    valid_to: Optional[datetime.datetime] = None
    # The vat property
    vat: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsSettlementUpgradeQuote:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsSettlementUpgradeQuote
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsSettlementUpgradeQuote()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ls_quote_type import LsQuoteType

        from .ls_quote_type import LsQuoteType

        fields: dict[str, Callable[[Any], None]] = {
            "arrears": lambda n : setattr(self, 'arrears', n.get_float_value()),
            "balance": lambda n : setattr(self, 'balance', n.get_float_value()),
            "discount": lambda n : setattr(self, 'discount', n.get_float_value()),
            "netSettlement": lambda n : setattr(self, 'net_settlement', n.get_float_value()),
            "quoteType": lambda n : setattr(self, 'quote_type', n.get_enum_value(LsQuoteType)),
            "settlementFee": lambda n : setattr(self, 'settlement_fee', n.get_float_value()),
            "total": lambda n : setattr(self, 'total', n.get_float_value()),
            "validTo": lambda n : setattr(self, 'valid_to', n.get_datetime_value()),
            "vat": lambda n : setattr(self, 'vat', n.get_float_value()),
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
        writer.write_float_value("arrears", self.arrears)
        writer.write_float_value("balance", self.balance)
        writer.write_float_value("discount", self.discount)
        writer.write_float_value("netSettlement", self.net_settlement)
        writer.write_enum_value("quoteType", self.quote_type)
        writer.write_float_value("settlementFee", self.settlement_fee)
        writer.write_float_value("total", self.total)
        writer.write_datetime_value("validTo", self.valid_to)
        writer.write_float_value("vat", self.vat)
    

