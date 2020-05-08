from abc import ABC, abstractmethod
import dataclasses
import logging

from data_classes import *
import constants as cc
import helpers
from exceptions import ProcessorError

logger = logging.getLogger(__name__)

"""
A resource consists of the following things:

1. A dataclass for validating the data coming from the database.
2. A process function that takes a record coming from the database and returns a processed record in the form we want to send to Twilio
3. A message_format string that can be passed data with the .format method.
"""


class Resource(ABC):
    @property
    @abstractmethod
    def dataclass(self):
        pass

    @property
    @abstractmethod
    def message_format(self):
        pass

    def __init__(self, record):
        self.record = record
        self.name = record[cc.RESOURCE_NAME_FIELD_NAME]
        self._validated_record = None

    @abstractmethod
    def process(self):
        pass

    def validate(self):
        fields = [field.name for field in dataclasses.fields(self.dataclass)]
        subsetted_record = {
            field: value for field, value in self.record.items() if field in fields
        }
        try:
            self.dataclass(**subsetted_record)
            self._validated_record = subsetted_record
            return subsetted_record
        except TypeError:
            logger.exception(
                f"{subsetted_record} is not a valid {self.dataclass.__name__}"
            )
            raise TypeError

    def create_message(self):
        try:
            validated_record = self.validate()
            processed_record = self.process(validated_record)
        except:
            logger.exception(
                f"{validated_record} failed in processing. Type={self.__class__.__name__}"
            )
            raise ProcessorError
        return self.message_format.format(**processed_record)

    @property
    def validated_record(self):
        if self._validated_record:
            return self._validated_record
        else:
            validated_record = self.validate()
            return validated_record


class GenericResource(Resource):

    dataclass = GeneralDataClass

    message_format = cc.Messages.GENERAL_MESSAGE

    def process(self, record):
        record["status"] = helpers.convert_status(record["status"])
        return record
    
class FarmResource(Resource):

    dataclass = FarmDataClass

    message_format = cc.Messages.FARM_MESSAGE

    def process(self, record):
        return record
