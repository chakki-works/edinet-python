from datetime import datetime
from edinet.reader.base_parser import BaseParser
from edinet.reader.edinet.edinet_value import EDINETValue


class Metadata(BaseParser):

    def __init__(self, reader):
        tags = {
            "fiscal_date": "jpdei_cor:CurrentFiscalYearStartDateDEI",
            "fiscal_period_kind": "jpdei_cor:TypeOfCurrentPeriodDEI",
            "name": "jpcrp_cor:CompanyNameCoverPage",
            "name_en": "jpcrp_cor:CompanyNameInEnglishCoverPage",
            "address": "jpcrp_cor:AddressOfRegisteredHeadquarterCoverPage",
            "phone_number": "jpcrp_cor:TelephoneNumberAddressOfRegisteredHeadquarterCoverPage"
        }

        super().__init__(reader, tags)

    @property
    def fiscal_year(self):
        value = self.get_text_value("fiscal_date")
        if value:
            date = datetime.strptime(value.value, "%Y-%m-%d")
            value.value = date.year
        return value

    @property
    def fiscal_month(self):
        value = self.get_text_value("fiscal_date")
        if value:
            date = datetime.strptime(value.value, "%Y-%m-%d")
            value.value = date.month
        return value

    @property
    def fiscal_period_kind(self):
        return self.get_text_value("fiscal_period_kind")

    @property
    def company_name(self):
        return self.get_text_value("name")

    @property
    def company_name_en(self):
        return self.get_text_value("name_en")

    @property
    def address(self):
        return self.get_text_value("address")

    @property
    def phone_number(self):
        return self.get_text_value("phone_number")
