import requests
import json

pokemon_req = requests.get("https://pokeapi.co/api/v2/pokemon/dragonite")

# data_dict = pokemon_req.json()
# print(data_dict)

poke_data = json.loads(pokemon_req.text)
# print(type(poke_data))
print(poke_data["name"])
