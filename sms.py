from twilio.rest import Client
"""
Send messages with twilio
"""
account_sid = 'account_sid_from_twilio'
auth_token = 'auth_token _from_twilio'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='messaging_service_sid_from_twilio',
    body='text message to be sent',
    to='to_phone_number'
)

print(message.sid)
