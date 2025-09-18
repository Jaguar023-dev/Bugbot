from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, jsonify
import os
import uuid
import pyfiglet
account_sid = 'YOUR_ACCOUNT_SID' 
auth_token = 'YOUR_AUTH_TOKEN' 
client = Client(account_sid, auth_token)
app = Flask(__name__)
def generate_session():
    session_id = str(uuid.uuid4())
    return session_id
def scanner(message):
    if message.lower() == 'scan':
        response = MessagingResponse()
        response.message(body='Send me the QR code or type "generate" to generate session.')
        return str(response)
    elif message.lower() == 'generate':
        session_id = generate_session()
        response = MessagingResponse()
        qr_code = pyfiglet.figlet_format(session_id)
        response.message(body=f'Here is your session ID:
{qr_code}')
        return str(response)
    else:
        return None
def handle_incoming():
    incoming_msg = request.values.get('Body', None)
    response = MessagingResponse()
    response.message(body='Hello, thanks for messaging!')
    return str(response)
@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', None)
    return scanner(incoming_msg) or handle_incoming()
if __name__ == '__main__':
    app.run(debug=True).

def scanner(message):
    if message.lower() == 'scan':
        response = MessagingResponse()
        response.message(body='Send me the QR code or type "generate" to generate session.')
        return str(response)
    elif message.lower() == 'generate':
        session_id = generate_session()
        response = MessagingResponse()
        qr_code = pyfiglet.figlet_format(session_id)
        response.message(body=f'Here is your session ID:
{qr_code}')
        return str(response)
```
