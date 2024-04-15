# Parse json

import json

# .load() example

# with open("car_data.json") as jsonfile:
#     car = json.load(jsonfile) # converting data in json file to a dictonary
#     print(type(car))
#     print(car["name"])
#     print(car["engine"])

# .loads() example

path_to_json = "example.json"
json = json.loads(open(path_to_json).read())
value = json["name"]
print(value)

# json.load() takes a file
# json.loads() takes a string