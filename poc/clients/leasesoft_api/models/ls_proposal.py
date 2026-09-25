from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ls_address import LsAddress

@dataclass
class LsProposal(Parsable):
    # The agreementNumber property
    agreement_number: Optional[str] = None
    # The agreementType property
    agreement_type: Optional[str] = None
    # The assetCost property
    asset_cost: Optional[float] = None
    # The balloon property
    balloon: Optional[float] = None
    # The brokerCompanyName property
    broker_company_name: Optional[str] = None
    # The companyRegistrationNumber property
    company_registration_number: Optional[str] = None
    # The companyType property
    company_type: Optional[str] = None
    # The dateEstablished property
    date_established: Optional[datetime.datetime] = None
    # The deposit property
    deposit: Optional[float] = None
    # The partExchange property
    part_exchange: Optional[float] = None
    # The profile property
    profile: Optional[str] = None
    # The registeredAddress property
    registered_address: Optional[LsAddress] = None
    # The schema property
    schema: Optional[str] = None
    # The term property
    term: Optional[int] = None
    # The tradingAddress property
    trading_address: Optional[LsAddress] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsProposal:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsProposal
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsProposal()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ls_address import LsAddress

        from .ls_address import LsAddress

        fields: dict[str, Callable[[Any], None]] = {
            "agreementNumber": lambda n : setattr(self, 'agreement_number', n.get_str_value()),
            "agreementType": lambda n : setattr(self, 'agreement_type', n.get_str_value()),
            "assetCost": lambda n : setattr(self, 'asset_cost', n.get_float_value()),
            "balloon": lambda n : setattr(self, 'balloon', n.get_float_value()),
            "brokerCompanyName": lambda n : setattr(self, 'broker_company_name', n.get_str_value()),
            "companyRegistrationNumber": lambda n : setattr(self, 'company_registration_number', n.get_str_value()),
            "companyType": lambda n : setattr(self, 'company_type', n.get_str_value()),
            "dateEstablished": lambda n : setattr(self, 'date_established', n.get_datetime_value()),
            "deposit": lambda n : setattr(self, 'deposit', n.get_float_value()),
            "partExchange": lambda n : setattr(self, 'part_exchange', n.get_float_value()),
            "profile": lambda n : setattr(self, 'profile', n.get_str_value()),
            "registeredAddress": lambda n : setattr(self, 'registered_address', n.get_object_value(LsAddress)),
            "schema": lambda n : setattr(self, 'schema', n.get_str_value()),
            "term": lambda n : setattr(self, 'term', n.get_int_value()),
            "tradingAddress": lambda n : setattr(self, 'trading_address', n.get_object_value(LsAddress)),
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
        writer.write_str_value("agreementNumber", self.agreement_number)
        writer.write_str_value("agreementType", self.agreement_type)
        writer.write_float_value("assetCost", self.asset_cost)
        writer.write_float_value("balloon", self.balloon)
        writer.write_str_value("brokerCompanyName", self.broker_company_name)
        writer.write_str_value("companyRegistrationNumber", self.company_registration_number)
        writer.write_str_value("companyType", self.company_type)
        writer.write_datetime_value("dateEstablished", self.date_established)
        writer.write_float_value("deposit", self.deposit)
        writer.write_float_value("partExchange", self.part_exchange)
        writer.write_str_value("profile", self.profile)
        writer.write_object_value("registeredAddress", self.registered_address)
        writer.write_str_value("schema", self.schema)
        writer.write_int_value("term", self.term)
        writer.write_object_value("tradingAddress", self.trading_address)
    

