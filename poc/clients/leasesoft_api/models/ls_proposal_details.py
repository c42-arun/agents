from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ls_address import LsAddress
    from .ls_asset_details import LsAssetDetails
    from .ls_guarantor import LsGuarantor
    from .ls_person import LsPerson
    from .ls_sole_trader import LsSoleTrader

@dataclass
class LsProposalDetails(Parsable):
    # The additionalInfo property
    additional_info: Optional[str] = None
    # The agreementNumber property
    agreement_number: Optional[str] = None
    # The agreementType property
    agreement_type: Optional[str] = None
    # The assetDetails property
    asset_details: Optional[list[LsAssetDetails]] = None
    # The balloonAmount property
    balloon_amount: Optional[float] = None
    # The brokerCompanyName property
    broker_company_name: Optional[str] = None
    # The companyName property
    company_name: Optional[str] = None
    # The companyRegistrationNumber property
    company_registration_number: Optional[str] = None
    # The companyTradingAs property
    company_trading_as: Optional[str] = None
    # The companyType property
    company_type: Optional[str] = None
    # The dateEstablished property
    date_established: Optional[datetime.datetime] = None
    # The deposit property
    deposit: Optional[float] = None
    # The guarantors property
    guarantors: Optional[list[LsGuarantor]] = None
    # The loanDetails property
    loan_details: Optional[LsAssetDetails] = None
    # The partExchange property
    part_exchange: Optional[float] = None
    # The partners property
    partners: Optional[list[LsPerson]] = None
    # The paymentFrequency property
    payment_frequency: Optional[str] = None
    # The paymentMethod property
    payment_method: Optional[str] = None
    # The profile property
    profile: Optional[str] = None
    # The proposalNotes property
    proposal_notes: Optional[str] = None
    # The registeredAddress property
    registered_address: Optional[LsAddress] = None
    # The schema property
    schema: Optional[str] = None
    # The settlement property
    settlement: Optional[float] = None
    # The soleTrader property
    sole_trader: Optional[LsSoleTrader] = None
    # The term property
    term: Optional[int] = None
    # The totalEquipmentCost property
    total_equipment_cost: Optional[float] = None
    # The tradingAddress property
    trading_address: Optional[LsAddress] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsProposalDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsProposalDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsProposalDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ls_address import LsAddress
        from .ls_asset_details import LsAssetDetails
        from .ls_guarantor import LsGuarantor
        from .ls_person import LsPerson
        from .ls_sole_trader import LsSoleTrader

        from .ls_address import LsAddress
        from .ls_asset_details import LsAssetDetails
        from .ls_guarantor import LsGuarantor
        from .ls_person import LsPerson
        from .ls_sole_trader import LsSoleTrader

        fields: dict[str, Callable[[Any], None]] = {
            "additionalInfo": lambda n : setattr(self, 'additional_info', n.get_str_value()),
            "agreementNumber": lambda n : setattr(self, 'agreement_number', n.get_str_value()),
            "agreementType": lambda n : setattr(self, 'agreement_type', n.get_str_value()),
            "assetDetails": lambda n : setattr(self, 'asset_details', n.get_collection_of_object_values(LsAssetDetails)),
            "balloonAmount": lambda n : setattr(self, 'balloon_amount', n.get_float_value()),
            "brokerCompanyName": lambda n : setattr(self, 'broker_company_name', n.get_str_value()),
            "companyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "companyRegistrationNumber": lambda n : setattr(self, 'company_registration_number', n.get_str_value()),
            "companyTradingAs": lambda n : setattr(self, 'company_trading_as', n.get_str_value()),
            "companyType": lambda n : setattr(self, 'company_type', n.get_str_value()),
            "dateEstablished": lambda n : setattr(self, 'date_established', n.get_datetime_value()),
            "deposit": lambda n : setattr(self, 'deposit', n.get_float_value()),
            "guarantors": lambda n : setattr(self, 'guarantors', n.get_collection_of_object_values(LsGuarantor)),
            "loanDetails": lambda n : setattr(self, 'loan_details', n.get_object_value(LsAssetDetails)),
            "partExchange": lambda n : setattr(self, 'part_exchange', n.get_float_value()),
            "partners": lambda n : setattr(self, 'partners', n.get_collection_of_object_values(LsPerson)),
            "paymentFrequency": lambda n : setattr(self, 'payment_frequency', n.get_str_value()),
            "paymentMethod": lambda n : setattr(self, 'payment_method', n.get_str_value()),
            "profile": lambda n : setattr(self, 'profile', n.get_str_value()),
            "proposalNotes": lambda n : setattr(self, 'proposal_notes', n.get_str_value()),
            "registeredAddress": lambda n : setattr(self, 'registered_address', n.get_object_value(LsAddress)),
            "schema": lambda n : setattr(self, 'schema', n.get_str_value()),
            "settlement": lambda n : setattr(self, 'settlement', n.get_float_value()),
            "soleTrader": lambda n : setattr(self, 'sole_trader', n.get_object_value(LsSoleTrader)),
            "term": lambda n : setattr(self, 'term', n.get_int_value()),
            "totalEquipmentCost": lambda n : setattr(self, 'total_equipment_cost', n.get_float_value()),
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
        writer.write_str_value("additionalInfo", self.additional_info)
        writer.write_str_value("agreementNumber", self.agreement_number)
        writer.write_str_value("agreementType", self.agreement_type)
        writer.write_collection_of_object_values("assetDetails", self.asset_details)
        writer.write_float_value("balloonAmount", self.balloon_amount)
        writer.write_str_value("brokerCompanyName", self.broker_company_name)
        writer.write_str_value("companyName", self.company_name)
        writer.write_str_value("companyRegistrationNumber", self.company_registration_number)
        writer.write_str_value("companyTradingAs", self.company_trading_as)
        writer.write_str_value("companyType", self.company_type)
        writer.write_datetime_value("dateEstablished", self.date_established)
        writer.write_float_value("deposit", self.deposit)
        writer.write_collection_of_object_values("guarantors", self.guarantors)
        writer.write_object_value("loanDetails", self.loan_details)
        writer.write_float_value("partExchange", self.part_exchange)
        writer.write_collection_of_object_values("partners", self.partners)
        writer.write_str_value("paymentFrequency", self.payment_frequency)
        writer.write_str_value("paymentMethod", self.payment_method)
        writer.write_str_value("profile", self.profile)
        writer.write_str_value("proposalNotes", self.proposal_notes)
        writer.write_object_value("registeredAddress", self.registered_address)
        writer.write_str_value("schema", self.schema)
        writer.write_float_value("settlement", self.settlement)
        writer.write_object_value("soleTrader", self.sole_trader)
        writer.write_int_value("term", self.term)
        writer.write_float_value("totalEquipmentCost", self.total_equipment_cost)
        writer.write_object_value("tradingAddress", self.trading_address)
    

