from twilio.rest import Client

def send_sms_notification(to, body):
    account_sid = 'your_twilio_account_sid'
    auth_token = 'your_twilio_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_='+your_twilio_number',
        to=to
    )

    return message.sid
