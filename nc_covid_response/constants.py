class TabNames:
    TEST_DATA = "sms_test_data"


ACTIVE_TABS = [
    TabNames.TEST_DATA,
]

PHONE_NUMBER_FIELD_NAME = "sms_contact"
RESOURCE_NAME_FIELD_NAME = "provider_name"


class Messages:
    GENERAL_MESSAGE = f"""
Name: {{provider_name}}
Status: {{status}}
Hours:
    Sun: {{sun}} 
    Mon: {{mon}}
    Tues: {{tues}}
    Wed: {{wed}}
    Thurs: {{thr}}
    Fri: {{fri}}
    Sat: {{sat}}
Offers: {{offers}}
    ""
    
    FARM_MESSAGE = f"""
Name: {{provider_name}}
Instructions to customers: {{instructions}} 
    """
