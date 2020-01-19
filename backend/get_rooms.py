import requests
from datetime import  date, datetime, time, timedelta
import json

params = {
  "token": "uclapi-18eefea61aa8f4b-3ee8f19755065c5-4531c2d5bd84479-d325162d470dda7",
  "start_datetime": (datetime.now() + timedelta(days=3, hours= 8)).isoformat(),
  "end_datetime": (datetime.now() + timedelta(days=3, hours= 9)).isoformat()
}
print(params["start_datetime"])
r = requests.get("https://uclapi.com/roombookings/freerooms", params=params)

result = r.json()["free_rooms"]

print(json.dumps([i for i in result if i["classification"] == "SS"],  sort_keys=True, indent=4))
