import json
import requests
import sso
import itemLookup
from requests.auth import HTTPBasicAuth

slack_token = sso.slack_token



# This constructs the message and formats it to look better for slack.
# def message(inData):
#   outMessage = ''
#   for item in inData: 
#     outMessage = outMessage + "*System ID:* {} \n*Moon ID:* {} \n*State:* {} \n".format(item["system_id"], item["moon_id"], item["state"]) + ("-"*60) + "\n"
#   return(outMessage)
# data = pull_starbases()
# #print(data)
# slack_message = message(data)
# print(slack_message)

# Posting the pre-formatted message to Slack
def postStuff(slack_message):
 header2 = {'User-Agent':"slack:Github\Memphypoos",'Authorization':'Bearer '+ slack_token, 'Content-Type': "application/json; charset=utf-8"}
 slack = requests.post("https://slack.com/api/chat.postMessage", headers=header2, data=json.dumps({'channel' : 'h0s_notifications', 'text': slack_message, 'as_user': 'true'}))
 print("Request posted to slack")
# postStuff(slack_message)
