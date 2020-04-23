import os
import requests
import json
import logging

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import constants as cc
from exceptions import ProcessorError
from resources import GenericResource

logger = logging.getLogger(__name__)


def send_sms(event, context):
    try:
        scope = ["https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json")
        client = gspread.authorize(creds)
        spreadsheet = client.open_by_key(os.environ["SPREADSHEET_KEY"])
    except gspread.exceptions.APIError:
        logger.exception(
            f"Unable to open spreadsheet with key {os.environ['SPREADSHEET_KEY']}"
        )
        raise
    for worksheet_name in cc.ACTIVE_TABS:
        try:
            worksheet = spreadsheet.worksheet(worksheet_name)
        except gspread.exceptions.WorksheetNotFound:
            logger.exception(
                f"Unable to find worksheet {worksheet_name} in spreadsheet {os.environ['SPREADSHEET_KEY']}"
            )
            continue

        records = worksheet.get_all_records()
        active_resource_class = GenericResource
        for i, record in enumerate(records):
            try:
                phone_number = record[cc.PHONE_NUMBER_FIELD_NAME]
            except KeyError:
                continue  # No phone number to text, so nothing to do.
            resource = active_resource_class(record)
            try:
                message = resource.create_message()
            except (TypeError, ProcessorError):
                continue
            params = json.dumps({"message": message, "name": resource.name})
            data = {
                "To": phone_number,
                "From": os.environ["TWILIO_NUMBER"],
                "Parameters": params,
            }
            try:
                response = requests.post(
                    os.environ["FLOW_URL"],
                    data=data,
                    auth=(
                        os.environ["TWILIO_ACCOUNT_SID"],
                        os.environ["TWILIO_AUTH_TOKEN"],
                    ),
                )
                response.raise_for_status()
            except:
                logger.info(
                    f"Row {i} raised status {response.status_code}. Record: {subsetted_record}"
                )
                continue
