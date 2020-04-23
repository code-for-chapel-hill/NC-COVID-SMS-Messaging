from dataclasses import dataclass


@dataclass
class GeneralDataClass:
    sms_contact: str
    provider_name: str = ""
    status: str = ""
    sun: str = ""
    mon: str = ""
    tues: str = ""
    wed: str = ""
    thr: str = ""
    fri: str = ""
    sat: str = ""
    offers: str = ""
