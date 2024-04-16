import requests

postcodes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
# print(postcodes_req)
# print(type(postcodes_req.status_code)) #200 int
# print(postcodes_req.headers)
# print(postcodes_req.content) # type: bytes -|
# print(postcodes_req.json()) # type: dict   --> both are the same but different types

data_dict = postcodes_req.json()["result"]
print(data_dict["region"])
