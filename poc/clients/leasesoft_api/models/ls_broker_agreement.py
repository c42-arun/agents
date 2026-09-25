from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ls_equipment import LsEquipment

@dataclass
class LsBrokerAgreement(Parsable):
    # The acceptanceReason property
    acceptance_reason: Optional[str] = None
    # The additionalSecurityTaken property
    additional_security_taken: Optional[str] = None
    # The brokerName property
    broker_name: Optional[str] = None
    # The clientName property
    client_name: Optional[str] = None
    # The contractType property
    contract_type: Optional[str] = None
    # The currency property
    currency: Optional[str] = None
    # The equipment property
    equipment: Optional[list[LsEquipment]] = None
    # The investecRef property
    investec_ref: Optional[str] = None
    # The numberOfYearsTrading property
    number_of_years_trading: Optional[str] = None
    # The originalCost property
    original_cost: Optional[float] = None
    # The period property
    period: Optional[int] = None
    # The profile property
    profile: Optional[str] = None
    # The proposalDate property
    proposal_date: Optional[datetime.datetime] = None
    # The proposalValidToDate property
    proposal_valid_to_date: Optional[datetime.datetime] = None
    # The qualityCategory property
    quality_category: Optional[str] = None
    # The settlementDate property
    settlement_date: Optional[datetime.datetime] = None
    # The status property
    status: Optional[str] = None
    # The statusDate property
    status_date: Optional[datetime.datetime] = None
    # The subStatus property
    sub_status: Optional[str] = None
    # The summary property
    summary: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsBrokerAgreement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsBrokerAgreement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsBrokerAgreement()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ls_equipment import LsEquipment

        from .ls_equipment import LsEquipment

        fields: dict[str, Callable[[Any], None]] = {
            "acceptanceReason": lambda n : setattr(self, 'acceptance_reason', n.get_str_value()),
            "additionalSecurityTaken": lambda n : setattr(self, 'additional_security_taken', n.get_str_value()),
            "brokerName": lambda n : setattr(self, 'broker_name', n.get_str_value()),
            "clientName": lambda n : setattr(self, 'client_name', n.get_str_value()),
            "contractType": lambda n : setattr(self, 'contract_type', n.get_str_value()),
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "equipment": lambda n : setattr(self, 'equipment', n.get_collection_of_object_values(LsEquipment)),
            "investecRef": lambda n : setattr(self, 'investec_ref', n.get_str_value()),
            "numberOfYearsTrading": lambda n : setattr(self, 'number_of_years_trading', n.get_str_value()),
            "originalCost": lambda n : setattr(self, 'original_cost', n.get_float_value()),
            "period": lambda n : setattr(self, 'period', n.get_int_value()),
            "profile": lambda n : setattr(self, 'profile', n.get_str_value()),
            "proposalDate": lambda n : setattr(self, 'proposal_date', n.get_datetime_value()),
            "proposalValidToDate": lambda n : setattr(self, 'proposal_valid_to_date', n.get_datetime_value()),
            "qualityCategory": lambda n : setattr(self, 'quality_category', n.get_str_value()),
            "settlementDate": lambda n : setattr(self, 'settlement_date', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "statusDate": lambda n : setattr(self, 'status_date', n.get_datetime_value()),
            "subStatus": lambda n : setattr(self, 'sub_status', n.get_str_value()),
            "summary": lambda n : setattr(self, 'summary', n.get_str_value()),
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
        writer.write_str_value("acceptanceReason", self.acceptance_reason)
        writer.write_str_value("additionalSecurityTaken", self.additional_security_taken)
        writer.write_str_value("brokerName", self.broker_name)
        writer.write_str_value("clientName", self.client_name)
        writer.write_str_value("contractType", self.contract_type)
        writer.write_str_value("currency", self.currency)
        writer.write_collection_of_object_values("equipment", self.equipment)
        writer.write_str_value("investecRef", self.investec_ref)
        writer.write_str_value("numberOfYearsTrading", self.number_of_years_trading)
        writer.write_float_value("originalCost", self.original_cost)
        writer.write_int_value("period", self.period)
        writer.write_str_value("profile", self.profile)
        writer.write_datetime_value("proposalDate", self.proposal_date)
        writer.write_datetime_value("proposalValidToDate", self.proposal_valid_to_date)
        writer.write_str_value("qualityCategory", self.quality_category)
        writer.write_datetime_value("settlementDate", self.settlement_date)
        writer.write_str_value("status", self.status)
        writer.write_datetime_value("statusDate", self.status_date)
        writer.write_str_value("subStatus", self.sub_status)
        writer.write_str_value("summary", self.summary)
    

