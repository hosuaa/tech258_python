import requests
import json

json_body = json.dumps({"postcodes": ["OX49 5NU", "M32 0JG", "NE30 1DP"]})
headers = {"Content-Type": "application/json"}
post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

print(post_multi_req.json())

# data= --> accepts a string (so we had to use json.dumps())
# json= --> accepts a python dictionary (so we wouldnt have to dumps() it first)
