import json
import requests
import configparser
import sso
import itemLookup
import postMsg
from requests.auth import HTTPBasicAuth

moons = {}
systems = {}
types = {}

config = configparser.ConfigParser()
config.read("config.ini")

refresh_token = config.get("config","refresh_token")
corp_id = config.get("config","corporation_id")
access_token = sso.refresh_esi_token(refresh_token)
header = {"User-Agent":"structureBot: github link here","Authorization":"Bearer "+access_token}
slack_token = config.get("config","slack_token")

pos = itemLookup.pull_starbases(corp_id)


for item in pos:
  breaker = ('-'*40)
  moon = item["moon_id"]
  posId = item["type_id"]
  ##print(posId)
  moonname = itemLookup.get_moon(moon)
  posName = itemLookup.get_type_name(posId) 
 # postMsg.postStuff(breaker)
  print(breaker)
  print("*Location:* {}".format(moonname))
  print("*Size*: {}" .format(posName))
  print("*Fueled till*: sysdate + timeleft")
  print(breaker)

# details = requests.get('https://esi.evetech.net/v1/corporations/'+str(corp_id)+'/starbases/'+str(pos['starbase_id'])+'/system_id='+str(pos['system_id']), headers=header).json()
# for fuel in details["fuels"]:
#   fuel_type = get_type(fuel["type_id"])
#   if "Block" in fuel_type["name"]:
#     hours = fuel["quantity"]/rate
#   if hours == 24: make_slack_call("*"+moon["name"]+"*\n_"+type["name"]+"_ has 24 hours of fuel remaining")
#   if hours > 0 and hours < 6:  make_slack_call("*"+moon["name"]+"*\n_"+type["name"]+"_ has less than 6 hours of fuel remaining")










