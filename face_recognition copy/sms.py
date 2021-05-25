# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

def check(s):
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
    account_sid = 'AC7bf87d90ed93ba492b7abc7abbefbb95'
    auth_token = '5ea8fdce8edd92b9859390f746782bb1'
    client = Client(account_sid, auth_token)

    add_ons_data = {"payfone_tcpa_compliance.RightPartyContactedDate": "20160101"}

    message = client.messages \
                    .create(
                        body="Python sms is working /n Aditya",
                        from_='+14159972407',
                        to='+91'+s
                    )

    print(message.sid)
