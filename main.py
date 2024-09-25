import configparser
from sendmail import *
import json
import time

config = configparser.ConfigParser()
config.read('config.ini')
try:
    attachments = json.loads(config['variables']['filer'])
    excludedemails = json.loads(config['variables']['excludedemails'])
    Startfromemail = config['variables']['Startfromemail']
    emaillist = slice_emails(getemaillist(), Startfromemail)
except:
    print("Please fill the config.ini correctly")


for email in emaillist:
    if (email not in excludedemails):
        sendmessage(email, createmessage(attachments))
        print(f"Email sent to: {email}")
    else:
        print(f"Email is excluded: {email}")

    time.sleep(10)
