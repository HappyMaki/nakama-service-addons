import os
import json

def load_gmail_creds():
    f = open("secrets/gmail_creds.secret", "r")
    data = json.loads("".join(f.readlines()))
    f.close()
    return data


GMAIL_CREDS = load_gmail_creds()
print(GMAIL_CREDS)