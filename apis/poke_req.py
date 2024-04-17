import requests
import json
import random


def pokemon_generator():
    return random.randint(1, 101)


def fetch_pokemon_data(pokemon_id):
    poke_req = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(pokemon_id))
    if poke_req.status_code == 200:
        return json.loads(poke_req.text)
    else:
        print("Error fetching Pokémon data. Please try again.")
        return None


def pokemon_compare(player_one, player_two):
    print(f"This is Player 1 height: {float(player_one['height']) * 10} cm")
    print(f"This is Player 2 height: {float(player_two['height']) * 10} cm")
    if player_one["height"] > player_two["height"]:
        return "Player one has won!"
    elif player_one["height"] == player_two["height"]:
        return "It's a draw!"
    else:
        return "Player two has won!"


while True:
    player_one_id = input("Player One, enter Pokémon ID (number 1-100): ")
    player_two_id = input("Player Two, enter Pokémon ID (number 1-100): ")
    print("Whoever is the tallest wins!")

    poke_data = fetch_pokemon_data(player_one_id)
    poke_data2 = fetch_pokemon_data(player_two_id)

    if poke_data and poke_data2:
        print(f"Player one: {poke_data['name']} (ノಠ益ಠ)ノ")
        print(f"Player two: {poke_data2['name']} (╯°□°）")

        print(pokemon_compare(poke_data, poke_data2))

    play_again_input = input("Do you want to play again? (yes/no): ").lower()
    if play_again_input != "yes":
        break