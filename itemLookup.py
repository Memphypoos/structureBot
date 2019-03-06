import json
import configparser
import sso
import requests

moons = {}
systems = {}
types = {}

refresh_token = sso.refresh_token
access_token = sso.refresh_esi_token(refresh_token)

header = {"User-Agent":"structureBot: github link here","Authorization":"Bearer "+access_token}

def pull_starbases(corp_id):
 corp_id = requests.get("https://esi.evetech.net/v1/corporations/"+ corp_id +"/starbases/", headers={'User-Agent':'FuelCheck','Authorization':'Bearer '+ str(access_token)})
 if corp_id.status_code == 200:
   return(corp_id.json())
 else:
   print(corp_id.status_code)

def get_moon(i):
  global moons
  if i in moons: 
    return moons[i]
  req = requests.get("https://esi.evetech.net/v1/universe/moons/"+str(i), headers=header)
  moons[i] = req.json()
  return req.json()["name"]

# "name"
# "security_status"
def get_system_name(i):
  global systems
  if i in systems:
    return systems[i]
  req = requests.get("https://esi.evetech.net/v4/universe/systems/"+str(i), headers=header)
  systems[i] = req.json()
  return req.json()["name"]# To add extra items to the list, uncomment this comment for an example #, req.json()["security_status"]

def get_type_name(i):
  req = requests.get("https://esi.evetech.net/latest/universe/types/"+str(i), headers=header)
  types[i] = req.json()
  return types[i]["name"]
