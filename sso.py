import json
import requests
from requests.auth import HTTPBasicAuth

#These are the Eve Developer API keys used to authenticate
eve_client = '337b56ed8dbd4c03b44963f303aa4360'
eve_secret_key = 'Sye1wCZzO7AXJyR5ktX39NXnb4t5WMVtEKOaRJqI'
login_server = 'https://login.eveonline.com/oauth/authorize?response_type=code&redirect_uri=https://localhost/callback&Client_id='
scopes = "esi-universe.read_structures.v1 esi-corporations.read_structures.v1 esi-characters.read_notifications.v1 esi-corporations.read_starbases.v1"
corp_id = '98088408'

refresh_token = 'V9NyH8pTDEP1PmthyEYWrgx3P3UIf-gURn4WpFCzbgu7sNRqBsz2KXeBz5Ewimtn0'
slack_token = 'xoxb-43069909811-393726398311-Qob5mPlB8wphOvL9QN9nxju4'




#Constructs the initial URL for the scopes
def constructUrl(login_server, eve_client, scopes):
  login_url = login_server+eve_client+"&scope="+scopes
  print(login_url) 

# This function refreshes the users access and provides a new ACCESS_CODE using the REFRESH_CODE.
def refresh_esi_token(refresh_token):
 req = requests.post('https://login.eveonline.com/oauth/token', auth=HTTPBasicAuth(eve_client,eve_secret_key), data={'grant_type':'refresh_token','refresh_token': refresh_token})
 if req.status_code == 200:
   
   return req.json()["access_token"]
   global access_token
   print("success")
 else:
   print(req.json())

def slack_key():
  config = configparser.ConfigParser()
  config.read("config.ini")