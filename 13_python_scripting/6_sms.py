# also this doesn't work because need to install twillio and sign up for an account.
# https://ntfy.sh/ can also use this site which makes it easy as well.

from twilio.rest import Client

account_sid = 'AC2d54c6f6d8c6331968ac2df10bfbc8c'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12266024690', body="hello", to='+17143304229')

print(message.sid)
