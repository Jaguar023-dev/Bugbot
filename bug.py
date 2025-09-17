```python
from pywhatsapp import Client
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
```