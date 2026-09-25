from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LsBankDetails(Parsable):
    # The accountName property
    account_name: Optional[str] = None
    # The accountNumber property
    account_number: Optional[str] = None
    # The accountSortCode property
    account_sort_code: Optional[str] = None
    # The collectionsBic property
    collections_bic: Optional[str] = None
    # The collectionsIban property
    collections_iban: Optional[str] = None
    # The creditorId property
    creditor_id: Optional[str] = None
    # The repaymentAccountCode property
    repayment_account_code: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsBankDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsBankDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsBankDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "accountName": lambda n : setattr(self, 'account_name', n.get_str_value()),
            "accountNumber": lambda n : setattr(self, 'account_number', n.get_str_value()),
            "accountSortCode": lambda n : setattr(self, 'account_sort_code', n.get_str_value()),
            "collectionsBic": lambda n : setattr(self, 'collections_bic', n.get_str_value()),
            "collectionsIban": lambda n : setattr(self, 'collections_iban', n.get_str_value()),
            "creditorId": lambda n : setattr(self, 'creditor_id', n.get_str_value()),
            "repaymentAccountCode": lambda n : setattr(self, 'repayment_account_code', n.get_str_value()),
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
        writer.write_str_value("accountName", self.account_name)
        writer.write_str_value("accountNumber", self.account_number)
        writer.write_str_value("accountSortCode", self.account_sort_code)
        writer.write_str_value("collectionsBic", self.collections_bic)
        writer.write_str_value("collectionsIban", self.collections_iban)
        writer.write_str_value("creditorId", self.creditor_id)
        writer.write_str_value("repaymentAccountCode", self.repayment_account_code)
    

