import dataclasses


from resources import *

test_record = {
    "resource": "fake_name",
    "provider_name": "Test Services",
    "status": 1,
}

test_farm_record = {
    "resource": "farm",
    "provider_name": "Test Farm",
    "instructions": "You do you"
}

class Tests:

    def test_generic_resource(self):
        resource = get_resource(test_record)
        assert isinstance(resource,GenericResource)
        message = resource.create_message()
        assert message == '\nName: Test Services\nStatus: Open\nHours:\n    Sun:  \n    Mon: \n    Tues: \n    Wed: \n    Thurs: \n    Fri: \n    Sat: \nOffers: \n    '

    def test_farm_resource(self): #Not testing message, since that's still subject to change
        resource = get_resource(test_farm_record)
        assert isinstance(resource,FarmResource)
        validated_record = resource.validated_record
        assert validated_record == {
            "provider_name": "Test Farm",
            "instructions": "You do you"
        }
    