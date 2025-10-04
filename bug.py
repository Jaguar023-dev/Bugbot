# from pydroid import api
# bug.py — WhatsApp bot using Twilio (ready for GitHub + Render)
import os
from twilio.rest import Client

def main():
    # === 1. Load environment variables ===
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    from_whatsapp = os.environ.get("TWILIO_WHATSAPP_FROM", "whatsapp:+14155238886")  # Twilio sandbox number
    to_whatsapp = os.environ.get("TWILIO_TEST_TO", "whatsapp:+254115953912")        # Your verified number

    if not account_sid or not auth_token:
        print("❌ Missing Twilio credentials! Set TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN in Render environment.")
        return

    # === 2. Initialize Twilio client ===
    client = Client(account_sid, auth_token)

    # === 3. Create and send message ===
    message_body = "Welcome to the new era of Vampire Rise MD — your next best WhatsApp bot!"
    message = client.messages.create(
        body=message_body,
        from_=from_whatsapp,
        to=to_whatsapp
    )

    # === 4. Print confirmation ===
    print("✅ Message sent successfully!")
    print("📨 Message SID:", message.sid)

if __name__ == "__main__":
    main()
def read_deleted(client):
    client.get_deleted_messages()
def send_without_save(client, number, message):
    client.send_message(number, message)
def hide_online(client, contacts):
    client.hide_online_status(contacts)
def use_multiple_accounts(client, accounts):
    for account in accounts:
        client.use_account(account)
def send_bulk(client, contacts, message):
    client.send_bulk_messages(contacts, message)
def auto_reply(client, message):
    client.auto_reply(message)
def schedule_message(client, number, message, time):
    client.schedule_message(number, message, time)
def clone_whatsapp(client, number):
    client.clone(number)
def prevent_account_takeover(client):
    client.prevent_account_takeover()
def bypass_two_factor_auth(client):
    client.bypass_two_factor_auth()
def unban_account(client, number):
    client.unban_account(number)
def view_private_status(client, number):
    client.view_private_status(number)
def crash_others_whatsapp(client, number):
    client.crash(number)
def automated_testing(client):
    client.test_automation()
def send_repeated_typing(client, number):
    client.repeated_typing(number)
def make_calls_fail(client, number):
    client.fail_calls(number)
def trigger_errors(client, number):
    client.trigger_errors(number)
def message_not_sent_loop(client, number):
    client.message_loop(number)
def crash_on_open_chat(client, number):
    client.crash_on_open(number)
def send_repeated_messages(client, number, message):
    client.repeated_messages(number, message)
def auto_download_statuses(client):
    client.auto_download()
def view_expired_statuses(client):
    client.view_expired()
def know_status_viewers(client):
    client.know_viewers()
def unban_banned_accounts(client, number):
    client.unban_account(number)
def view_all_chats_without_seen(client):
    client.view_all_chats()
def crash_others_whatsapp_again(client, number):
    client.crash(number)
def send_messages_as_contact(client, number, message, contact):
    client.send_as_contact(number, message, contact)
def change_whatsapp_theme(client, theme):
    client.change_theme(theme)
def use_custom_fonts(client, font):
    client.custom_fonts(font)
def send_messages_with_fake_time(client, number, message, time):
    client.fake_time(number, message, time)
def create_fake_groups(client, group_name, participants):
    client.fake_group(group_name, participants)
def add_anyone_to_group(client, group_name, participant):
    client.add_to_group(group_name, participant)
def view_all_chats_without_being_seen_again(client):
    client.view_all_chats()
def send_messages_with_custom_media(client, number, media):
    client.custom_media(number, media)
def make_video_calls_fail(client, number):
    client.fail_video_calls(number)
def change_whatsapp_colors(client, colors):
    client.change_colors(colors)
def use_custom_styles(client, style):
    client.custom_styles(style)
def send_messages_with_fake_timestamps(client, number, message, time):
    client.fake_timestamps(number, message, time)
def create_fake_conversations(client, number, messages):
    client.fake_conversations(number, messages)
def delete_all_messages_sent(client):
    client.delete_all_messages()
