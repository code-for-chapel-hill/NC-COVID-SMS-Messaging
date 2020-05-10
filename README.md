# nc-covid-response
This project is related to the NC Covid Support project: https://github.com/code-for-chapel-hill/NC-COVID-Support

This project is intended to automatically text message our business partners prompting them for updates to their business hours/offers/etc that should be reflected on https://nccovidsupport.org.

# Setup
You will need to generate a client_secret.json file and put it in the same directory as ask_for_updates.py in order to read from the Google sheet.

In order to do this:

1. Head to the Google Developers Console: https://console.developers.google.com/
2. Under “APIs & Services > Library”, search for “Drive API” and enable it.
3. Under “APIs & Services > Library”, search for “Sheets API” and enable it.
4. Go to “APIs & Services > Credentials” and choose “Create credentials > Service account”.

You should be able to generate a json file that looks something like this:
{
    "private_key_id": "2cd … ba4",
    "private_key": "-----BEGIN PRIVATE KEY-----\nNrDyLw … jINQh/9\n-----END PRIVATE KEY-----\n",
    "client_email": "473000000000-yoursisdifferent@developer.gserviceaccount.com",
    "client_id": "473 … hd.apps.googleusercontent.com",
    "type": "service_account"
    ...
}

Put that in the same directory as ask_for_updates.py.

Now run pip install -r requirements.txt in the base directory.

You will need to set the following environmental variables

    1. SPREADSHEET_KEY - They key of the google spreadsheet, which can be found in the URL
    2. TWILIO_NUMBER - the Twilio phone number we are using for texting
    3. FLOW_URL - the URL of the Twilio studio flow
    4. TWILIO_ACCOUNT_SID - get from twilio account
    5. TWILIO_AUTH_TOKEN - get from twilio account

# Deploy
This project is deployed as an AWS Lambda function. To deploy, zip the nc_covid_response directory (the directory with ask_for_updates.py) and use the AWS CLI to update the function code.

1. zip -r function.zip nc_covid_response/*
2. aws lambda update-function-code --function-name nc-covid-send-sms --zip-file fileb://function.zip

For more detailed instructions on setting up the AWS CLI and lambda-related CLI commands, see https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-awscli.html

# Update modules
The lambda function runs on top of an AWS layer containing all the necessary third-party Python modules. If you need to update or add a module, add that module to the modules directory with pip, then zip that to modules.zip, then use the AWS CLI to update the layer. Assuming you are in the base directory,

1. pip install package_name -t modules
2. zip -r modules.zip modules/*
3. aws lambda publish-layer-version --layer-name sms-packages --description "Packages for NC covid response SMS automated messaging" --zip-file fileb://modules.zip --compatible-runtimes python3.6 python3.7

You will then need to head into the AWS Lambda consol and click on 'Layers' in the 'Designer' box. Change the version of the layer to the latest version.

# Creating a new resource
The data is split into different types of resources (farms, restaurants, etc.) The messages sent to different types of resources can be customized by creating a new resource class. See the abstract base class and docstring in resources.py for details.