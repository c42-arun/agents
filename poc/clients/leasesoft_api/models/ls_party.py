from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ls_party_credit_report import LsPartyCreditReport
    from .ls_primary_contact_details import LsPrimaryContactDetails

@dataclass
class LsParty(Parsable):
    # The addressLine1 property
    address_line1: Optional[str] = None
    # The addressLine2 property
    address_line2: Optional[str] = None
    # The addressLine3 property
    address_line3: Optional[str] = None
    # The addressLine4 property
    address_line4: Optional[str] = None
    # The addressType property
    address_type: Optional[str] = None
    # The addressTypeCode property
    address_type_code: Optional[str] = None
    # The amlNextReviewDate property
    aml_next_review_date: Optional[datetime.datetime] = None
    # The amlStatus property
    aml_status: Optional[str] = None
    # The analysisCode2 property
    analysis_code2: Optional[str] = None
    # The analysisCode3 property
    analysis_code3: Optional[str] = None
    # The analysisCode4 property
    analysis_code4: Optional[str] = None
    # The analysisCode5 property
    analysis_code5: Optional[str] = None
    # The analysisCode6 property
    analysis_code6: Optional[str] = None
    # The atAddressSince property
    at_address_since: Optional[datetime.datetime] = None
    # The averageBaseRate property
    average_base_rate: Optional[float] = None
    # The brokerManagement property
    broker_management: Optional[str] = None
    # The companyRegistration property
    company_registration: Optional[str] = None
    # The contactDetails property
    contact_details: Optional[LsPrimaryContactDetails] = None
    # The country property
    country: Optional[str] = None
    # The countryIsoCode property
    country_iso_code: Optional[str] = None
    # The countyCode property
    county_code: Optional[str] = None
    # The creditDetailAutocode property
    credit_detail_autocode: Optional[float] = None
    # The creditLineAmount property
    credit_line_amount: Optional[float] = None
    # The creditLineType property
    credit_line_type: Optional[str] = None
    # The creditLineTypeCode property
    credit_line_type_code: Optional[str] = None
    # The creditRating property
    credit_rating: Optional[str] = None
    # The creditReport property
    credit_report: Optional[LsPartyCreditReport] = None
    # The creditRiskStatus property
    credit_risk_status: Optional[str] = None
    # The creditRiskStatusCode property
    credit_risk_status_code: Optional[str] = None
    # The currency property
    currency: Optional[str] = None
    # The dateApproved property
    date_approved: Optional[datetime.datetime] = None
    # The dateExpires property
    date_expires: Optional[datetime.datetime] = None
    # The dateIncorporated property
    date_incorporated: Optional[datetime.datetime] = None
    # The dateLatestAccounts property
    date_latest_accounts: Optional[datetime.datetime] = None
    # The dateNextReview property
    date_next_review: Optional[datetime.datetime] = None
    # The dateOfBirth property
    date_of_birth: Optional[datetime.datetime] = None
    # The drawdownPeriod property
    drawdown_period: Optional[str] = None
    # The firstName property
    first_name: Optional[str] = None
    # The flatNo property
    flat_no: Optional[str] = None
    # The goldenRecord property
    golden_record: Optional[str] = None
    # The guaranteeTypeCode property
    guarantee_type_code: Optional[str] = None
    # The guaranteeTypeDescription property
    guarantee_type_description: Optional[str] = None
    # The houseNo property
    house_no: Optional[str] = None
    # The latestAccountType property
    latest_account_type: Optional[str] = None
    # The latestAccountTypeCode property
    latest_account_type_code: Optional[str] = None
    # The modifiedDate property
    modified_date: Optional[datetime.datetime] = None
    # The moneyLaunderingCode property
    money_laundering_code: Optional[str] = None
    # The notUsedCreditLimit property
    not_used_credit_limit: Optional[float] = None
    # The notUsedCreditLimitReviewDate property
    not_used_credit_limit_review_date: Optional[datetime.datetime] = None
    # The otherName property
    other_name: Optional[str] = None
    # The partyShortNameCode property
    party_short_name_code: Optional[str] = None
    # The postCode property
    post_code: Optional[str] = None
    # The primaryContactName property
    primary_contact_name: Optional[str] = None
    # The primaryContactNumber property
    primary_contact_number: Optional[str] = None
    # The primaryRelationshipCode property
    primary_relationship_code: Optional[str] = None
    # The qualifyingTerms property
    qualifying_terms: Optional[str] = None
    # The redactionStatusCode property
    redaction_status_code: Optional[str] = None
    # The role property
    role: Optional[str] = None
    # The sicCode property
    sic_code: Optional[str] = None
    # The sicCodeDescription property
    sic_code_description: Optional[str] = None
    # The smeExceptionsCode property
    sme_exceptions_code: Optional[str] = None
    # The sstCode property
    sst_code: Optional[str] = None
    # The surname property
    surname: Optional[str] = None
    # The title property
    title: Optional[str] = None
    # The tradingAs property
    trading_as: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LsParty:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LsParty
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LsParty()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ls_party_credit_report import LsPartyCreditReport
        from .ls_primary_contact_details import LsPrimaryContactDetails

        from .ls_party_credit_report import LsPartyCreditReport
        from .ls_primary_contact_details import LsPrimaryContactDetails

        fields: dict[str, Callable[[Any], None]] = {
            "addressLine1": lambda n : setattr(self, 'address_line1', n.get_str_value()),
            "addressLine2": lambda n : setattr(self, 'address_line2', n.get_str_value()),
            "addressLine3": lambda n : setattr(self, 'address_line3', n.get_str_value()),
            "addressLine4": lambda n : setattr(self, 'address_line4', n.get_str_value()),
            "addressType": lambda n : setattr(self, 'address_type', n.get_str_value()),
            "addressTypeCode": lambda n : setattr(self, 'address_type_code', n.get_str_value()),
            "amlNextReviewDate": lambda n : setattr(self, 'aml_next_review_date', n.get_datetime_value()),
            "amlStatus": lambda n : setattr(self, 'aml_status', n.get_str_value()),
            "analysisCode2": lambda n : setattr(self, 'analysis_code2', n.get_str_value()),
            "analysisCode3": lambda n : setattr(self, 'analysis_code3', n.get_str_value()),
            "analysisCode4": lambda n : setattr(self, 'analysis_code4', n.get_str_value()),
            "analysisCode5": lambda n : setattr(self, 'analysis_code5', n.get_str_value()),
            "analysisCode6": lambda n : setattr(self, 'analysis_code6', n.get_str_value()),
            "atAddressSince": lambda n : setattr(self, 'at_address_since', n.get_datetime_value()),
            "averageBaseRate": lambda n : setattr(self, 'average_base_rate', n.get_float_value()),
            "brokerManagement": lambda n : setattr(self, 'broker_management', n.get_str_value()),
            "companyRegistration": lambda n : setattr(self, 'company_registration', n.get_str_value()),
            "contactDetails": lambda n : setattr(self, 'contact_details', n.get_object_value(LsPrimaryContactDetails)),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "countryIsoCode": lambda n : setattr(self, 'country_iso_code', n.get_str_value()),
            "countyCode": lambda n : setattr(self, 'county_code', n.get_str_value()),
            "creditDetailAutocode": lambda n : setattr(self, 'credit_detail_autocode', n.get_float_value()),
            "creditLineAmount": lambda n : setattr(self, 'credit_line_amount', n.get_float_value()),
            "creditLineType": lambda n : setattr(self, 'credit_line_type', n.get_str_value()),
            "creditLineTypeCode": lambda n : setattr(self, 'credit_line_type_code', n.get_str_value()),
            "creditRating": lambda n : setattr(self, 'credit_rating', n.get_str_value()),
            "creditReport": lambda n : setattr(self, 'credit_report', n.get_object_value(LsPartyCreditReport)),
            "creditRiskStatus": lambda n : setattr(self, 'credit_risk_status', n.get_str_value()),
            "creditRiskStatusCode": lambda n : setattr(self, 'credit_risk_status_code', n.get_str_value()),
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "dateApproved": lambda n : setattr(self, 'date_approved', n.get_datetime_value()),
            "dateExpires": lambda n : setattr(self, 'date_expires', n.get_datetime_value()),
            "dateIncorporated": lambda n : setattr(self, 'date_incorporated', n.get_datetime_value()),
            "dateLatestAccounts": lambda n : setattr(self, 'date_latest_accounts', n.get_datetime_value()),
            "dateNextReview": lambda n : setattr(self, 'date_next_review', n.get_datetime_value()),
            "dateOfBirth": lambda n : setattr(self, 'date_of_birth', n.get_datetime_value()),
            "drawdownPeriod": lambda n : setattr(self, 'drawdown_period', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "flatNo": lambda n : setattr(self, 'flat_no', n.get_str_value()),
            "goldenRecord": lambda n : setattr(self, 'golden_record', n.get_str_value()),
            "guaranteeTypeCode": lambda n : setattr(self, 'guarantee_type_code', n.get_str_value()),
            "guaranteeTypeDescription": lambda n : setattr(self, 'guarantee_type_description', n.get_str_value()),
            "houseNo": lambda n : setattr(self, 'house_no', n.get_str_value()),
            "latestAccountType": lambda n : setattr(self, 'latest_account_type', n.get_str_value()),
            "latestAccountTypeCode": lambda n : setattr(self, 'latest_account_type_code', n.get_str_value()),
            "modifiedDate": lambda n : setattr(self, 'modified_date', n.get_datetime_value()),
            "moneyLaunderingCode": lambda n : setattr(self, 'money_laundering_code', n.get_str_value()),
            "notUsedCreditLimit": lambda n : setattr(self, 'not_used_credit_limit', n.get_float_value()),
            "notUsedCreditLimitReviewDate": lambda n : setattr(self, 'not_used_credit_limit_review_date', n.get_datetime_value()),
            "otherName": lambda n : setattr(self, 'other_name', n.get_str_value()),
            "partyShortNameCode": lambda n : setattr(self, 'party_short_name_code', n.get_str_value()),
            "postCode": lambda n : setattr(self, 'post_code', n.get_str_value()),
            "primaryContactName": lambda n : setattr(self, 'primary_contact_name', n.get_str_value()),
            "primaryContactNumber": lambda n : setattr(self, 'primary_contact_number', n.get_str_value()),
            "primaryRelationshipCode": lambda n : setattr(self, 'primary_relationship_code', n.get_str_value()),
            "qualifyingTerms": lambda n : setattr(self, 'qualifying_terms', n.get_str_value()),
            "redactionStatusCode": lambda n : setattr(self, 'redaction_status_code', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_str_value()),
            "sicCode": lambda n : setattr(self, 'sic_code', n.get_str_value()),
            "sicCodeDescription": lambda n : setattr(self, 'sic_code_description', n.get_str_value()),
            "smeExceptionsCode": lambda n : setattr(self, 'sme_exceptions_code', n.get_str_value()),
            "sstCode": lambda n : setattr(self, 'sst_code', n.get_str_value()),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "tradingAs": lambda n : setattr(self, 'trading_as', n.get_str_value()),
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
        writer.write_str_value("addressLine3", self.address_line3)
        writer.write_str_value("addressLine4", self.address_line4)
        writer.write_str_value("addressType", self.address_type)
        writer.write_str_value("addressTypeCode", self.address_type_code)
        writer.write_datetime_value("amlNextReviewDate", self.aml_next_review_date)
        writer.write_str_value("amlStatus", self.aml_status)
        writer.write_str_value("analysisCode2", self.analysis_code2)
        writer.write_str_value("analysisCode3", self.analysis_code3)
        writer.write_str_value("analysisCode4", self.analysis_code4)
        writer.write_str_value("analysisCode5", self.analysis_code5)
        writer.write_str_value("analysisCode6", self.analysis_code6)
        writer.write_datetime_value("atAddressSince", self.at_address_since)
        writer.write_float_value("averageBaseRate", self.average_base_rate)
        writer.write_str_value("brokerManagement", self.broker_management)
        writer.write_str_value("companyRegistration", self.company_registration)
        writer.write_object_value("contactDetails", self.contact_details)
        writer.write_str_value("country", self.country)
        writer.write_str_value("countryIsoCode", self.country_iso_code)
        writer.write_str_value("countyCode", self.county_code)
        writer.write_float_value("creditDetailAutocode", self.credit_detail_autocode)
        writer.write_float_value("creditLineAmount", self.credit_line_amount)
        writer.write_str_value("creditLineType", self.credit_line_type)
        writer.write_str_value("creditLineTypeCode", self.credit_line_type_code)
        writer.write_str_value("creditRating", self.credit_rating)
        writer.write_object_value("creditReport", self.credit_report)
        writer.write_str_value("creditRiskStatus", self.credit_risk_status)
        writer.write_str_value("creditRiskStatusCode", self.credit_risk_status_code)
        writer.write_str_value("currency", self.currency)
        writer.write_datetime_value("dateApproved", self.date_approved)
        writer.write_datetime_value("dateExpires", self.date_expires)
        writer.write_datetime_value("dateIncorporated", self.date_incorporated)
        writer.write_datetime_value("dateLatestAccounts", self.date_latest_accounts)
        writer.write_datetime_value("dateNextReview", self.date_next_review)
        writer.write_datetime_value("dateOfBirth", self.date_of_birth)
        writer.write_str_value("drawdownPeriod", self.drawdown_period)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("flatNo", self.flat_no)
        writer.write_str_value("goldenRecord", self.golden_record)
        writer.write_str_value("guaranteeTypeCode", self.guarantee_type_code)
        writer.write_str_value("guaranteeTypeDescription", self.guarantee_type_description)
        writer.write_str_value("houseNo", self.house_no)
        writer.write_str_value("latestAccountType", self.latest_account_type)
        writer.write_str_value("latestAccountTypeCode", self.latest_account_type_code)
        writer.write_datetime_value("modifiedDate", self.modified_date)
        writer.write_str_value("moneyLaunderingCode", self.money_laundering_code)
        writer.write_float_value("notUsedCreditLimit", self.not_used_credit_limit)
        writer.write_datetime_value("notUsedCreditLimitReviewDate", self.not_used_credit_limit_review_date)
        writer.write_str_value("otherName", self.other_name)
        writer.write_str_value("partyShortNameCode", self.party_short_name_code)
        writer.write_str_value("postCode", self.post_code)
        writer.write_str_value("primaryContactName", self.primary_contact_name)
        writer.write_str_value("primaryContactNumber", self.primary_contact_number)
        writer.write_str_value("primaryRelationshipCode", self.primary_relationship_code)
        writer.write_str_value("qualifyingTerms", self.qualifying_terms)
        writer.write_str_value("redactionStatusCode", self.redaction_status_code)
        writer.write_str_value("role", self.role)
        writer.write_str_value("sicCode", self.sic_code)
        writer.write_str_value("sicCodeDescription", self.sic_code_description)
        writer.write_str_value("smeExceptionsCode", self.sme_exceptions_code)
        writer.write_str_value("sstCode", self.sst_code)
        writer.write_str_value("surname", self.surname)
        writer.write_str_value("title", self.title)
        writer.write_str_value("tradingAs", self.trading_as)
    

