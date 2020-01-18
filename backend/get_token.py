# import requests
#
# params = {
#   "client_id": "2520722774325931.7857694135946031",
#   "state": "1",
# }
# r = requests.get("https://uclapi.com/oauth/authorise", params=params)
# print(r)


import requests

params = {
  "client_id": "2520722774325931.7857694135946031",
  "code": "27456e59663cbf8f0e77c5b09c51c425786a91c66d6f17cff057b47cb8d1fc50",
  "client_secret": "27456e59663cbf8f0e77c5b09c51c425786a91c66d6f17cff057b47cb8d1fc50",
}
r = requests.get("https://uclapi.com/oauth/token", params=params)
print(r.json())
