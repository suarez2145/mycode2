#!/usr/bin/env python3

# importing flask 
from flask import Flask, render_template
# importing requests in order to make pokeapi call
import requests
# setting app name to Flask
app = Flask(__name__)
# defining route at "/" 
@app.route("/")
# defining our index function which will make the api call and return our render template which we have in templates folder
def index():
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon?offset=20&limit=10").json()
    newPokies = []
    newPokiesUrlData = []
    newPokeSprites = []
    # looping over our results from pokiapi data
    for poke in pokeapi["results"]:
        newPokies.append(poke['name'])
    for poke in pokeapi['results']:
        # making another requests from the URL within our Pokiapi request in order to retrieve icon sprite url
        newPokeData = requests.get(poke["url"]).json()
        newPokiesUrlData.append(newPokeData)
    print(newPokiesUrlData[0]["sprites"]["front_default"])

    for poke in newPokiesUrlData:
        newPokeSprites.append(poke["sprites"]["front_default"])
        
    # using zip to define new 'poke_sprite_arr' which combines poke and sprites arrays so i can loop over both simultaneously in my template
    return render_template("index.html", poke_sprite_arr=zip(newPokies, newPokeSprites))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=2224)
