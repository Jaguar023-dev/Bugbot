from modules.utils import init_whatsapp_session
from modules.chatbot import auto_reply

# Initialize session for this user's number
driver = init_whatsapp_session()

# Example loop to listen for incoming messages
while True:
    unread_messages = driver.get_unread_messages()  # implement per your bot
    for msg in unread_messages:
        reply = auto_reply(msg.text)
        driver.send_message(msg.sender, reply)