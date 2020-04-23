# nc-covid-response
This project is related to the NC Covid Support project: https://github.com/code-for-chapel-hill/NC-COVID-Support

This project is intended to automatically text message our business partners prompting them for updates to their business hours/offers/etc that should be reflected on https://nccovidsupport.org.

# Setup
You will need to generate a client_secret.json file and put it in the same directory as ask_for_updates.py.

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

# Deploy
This project is deployed as an AWS lambda.
In order to deploy, run deploy.sh from the base directory