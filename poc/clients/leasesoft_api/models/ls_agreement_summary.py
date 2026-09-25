from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ls_agreement_assets import LsAgreementAssets
    from .ls_business_line import LsBusinessLine
    from .ls_requester import LsRequester

@dataclass
class LsAgreementSummary(Parsable):
    # The agreementNo property
    agreement_no: Optional[str] = None
    # The allowActions property
    allow_actions: Optional[bool] = None
    # The arrearsValue property
    arrears_value: Optional[float] = None
    # The assets property
    assets: Optional[list[LsAgreementAssets]] = None
    # The brokerReference property
    broker_reference: Optional[str] = None
    # The businessLine property
    business_line: Optional[LsBusinessLine] = None
    # The contractType property
    contract_type: Optional[str] = None
    # The contractTypeCode property
    contract_type_code: Optional[str] = None
    # The isEnded property
    is_ended: Optional[bool] = None
    # The requester property
    requester: Optional[LsRequester] = None
    # The statusCode property
    status_code: Optional[str] = None
    # The statusDescription property
    status_description: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsAgreementSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsAgreementSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsAgreementSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ls_agreement_assets import LsAgreementAssets
        from .ls_business_line import LsBusinessLine
        from .ls_requester import LsRequester

        from .ls_agreement_assets import LsAgreementAssets
        from .ls_business_line import LsBusinessLine
        from .ls_requester import LsRequester

        fields: dict[str, Callable[[Any], None]] = {
            "agreementNo": lambda n : setattr(self, 'agreement_no', n.get_str_value()),
            "allowActions": lambda n : setattr(self, 'allow_actions', n.get_bool_value()),
            "arrearsValue": lambda n : setattr(self, 'arrears_value', n.get_float_value()),
            "assets": lambda n : setattr(self, 'assets', n.get_collection_of_object_values(LsAgreementAssets)),
            "brokerReference": lambda n : setattr(self, 'broker_reference', n.get_str_value()),
            "businessLine": lambda n : setattr(self, 'business_line', n.get_enum_value(LsBusinessLine)),
            "contractType": lambda n : setattr(self, 'contract_type', n.get_str_value()),
            "contractTypeCode": lambda n : setattr(self, 'contract_type_code', n.get_str_value()),
            "isEnded": lambda n : setattr(self, 'is_ended', n.get_bool_value()),
            "requester": lambda n : setattr(self, 'requester', n.get_enum_value(LsRequester)),
            "statusCode": lambda n : setattr(self, 'status_code', n.get_str_value()),
            "statusDescription": lambda n : setattr(self, 'status_description', n.get_str_value()),
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
        writer.write_str_value("agreementNo", self.agreement_no)
        writer.write_bool_value("allowActions", self.allow_actions)
        writer.write_float_value("arrearsValue", self.arrears_value)
        writer.write_collection_of_object_values("assets", self.assets)
        writer.write_str_value("brokerReference", self.broker_reference)
        writer.write_enum_value("businessLine", self.business_line)
        writer.write_str_value("contractType", self.contract_type)
        writer.write_str_value("contractTypeCode", self.contract_type_code)
        writer.write_bool_value("isEnded", self.is_ended)
        writer.write_enum_value("requester", self.requester)
        writer.write_str_value("statusCode", self.status_code)
        writer.write_str_value("statusDescription", self.status_description)
    

