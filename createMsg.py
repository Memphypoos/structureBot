import json
import requests
import sso
import itemLookup
from requests.auth import HTTPBasicAuth

def message(inData):
  outMessage = ''
  for item in inData:
    outMessage = outMessage + 



# This constructs the message and formats it to look better for slack.
def message(inData):
  outMessage = ''
  for item in inData: 
    outMessage = outMessage + "*System ID:* {} \n*Moon ID:* {} \n*State:* {} \n".format(item["system_id"], item["moon_id"], item["state"]) + ("-"*60) + "\n"
  return(outMessage)
data = pull_starbases()
#print(data)
slack_message = message(data)
print(slack_message)