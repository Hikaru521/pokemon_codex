import json
import requests
from tabulate import tabulate

input_text = input("Add meg a vizsgálandó pokemon ID-jét:")

def update_input_text():
    global input_text
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{input_text}")

    if response.status_code == 404:
        print("Pokemon not found")
        exit()

    x = json.loads(response.content)
    list_types = []
    list_ability_name = []
    list_name = [x["name"]]
    for i in x["types"]:
        list_types.append(i["type"]["name"])
    for i in x["abilities"]:
        list_ability_name.append(i["ability"]["name"])
    pokemons = ["Name", "Types", "Ability Name"],["\n".join(list_name), "\n".join(list_types), "\n".join(list_ability_name)]
    print(tabulate(pokemons, headers='firstrow', tablefmt='grid'))
    pokemons_basics = ["Hp", "Attack", "Deffense", "Special Attack", "Special Deffense", "Speed"], [x["stats"][0]["base_stat"], x["stats"][1]["base_stat"], x["stats"][2]["base_stat"],
                                                                                           x["stats"][3]["base_stat"], x["stats"][4]["base_stat"], x["stats"][5]["base_stat"]]
    print(tabulate(pokemons_basics, headers='firstrow', tablefmt='grid'))
    pokemons_weight_height = ["Weight", "Height"], [x["weight"], x["height"]]
    print(tabulate(pokemons_weight_height, headers='firstrow', tablefmt='grid'))
update_input_text()