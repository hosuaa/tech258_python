# JSON basics
import json

car_data = {
    "name": "tesla",
    "engine": "electric"
}
# cant just send this python dictionary to other apps -> use json
# json.dumps() --> serialises json to a formatted string

car_data_json_string = json.dumps(car_data)

# print(type(car_data)) # dict
# print(type(car_data_json_string)) # str

# json.dump() --> creates a stream object and expects a file object to write to
with open("car_data.json", "w") as jsonfile:
    json.dump(car_data, jsonfile)

# if you want to write your data to an external (json) file use dump
# if you want to work with the data in python use dumps (s for string)
