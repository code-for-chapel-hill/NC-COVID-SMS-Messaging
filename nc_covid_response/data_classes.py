from dataclasses import dataclass


@dataclass
class GenericDataClass:
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

@dataclass
class FarmDataClass:
    provider_name: str = ""
    instructions: str = ""
    
