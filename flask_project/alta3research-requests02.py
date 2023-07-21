#!/usr/bin/env python3

# importing flask 
from flask import Flask, render_template, flash
# importing requests in order to make pokeapi call
import requests
from flask import request
# setting app name to Flask
app = Flask(__name__)
app.secret_key = "super secret key"
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

    for poke in newPokiesUrlData:
        newPokeSprites.append(poke["sprites"]["front_default"])
        
    # using zip to define new 'poke_sprite_arr' which combines poke and sprites arrays so i can loop over both simultaneously in my template
    return render_template("index2.html", poke_sprite_arr=zip(newPokies, newPokeSprites))

@app.route("/pokesearch/newpoke",methods = ["POST"])
def pokesearch():
    if request.method == "POST":
        if request.form.get("pokename"):
            pokemonName = request.form.get("pokename").lower()
            getPoke = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemonName}')
            #  if statement to check for code 200
            if getPoke.status_code == 200:
                getPokeResult = getPoke.json()
                # creating a dictionary from the pokiapi data i returned
                pokeDict = {
                    'name':getPokeResult['name'],
                    'hp':getPokeResult['stats'][0]['base_stat'],
                    'atk':getPokeResult['stats'][1]['base_stat'],
                    'defns':getPokeResult['stats'][2]['base_stat'],
                    'icon':getPokeResult['sprites']['front_default']
                }
                # return the pokeresult page with the pokeDict dictionary as poke variable
                return render_template("pokeresults.html", poke = pokeDict )
            else:
                # using flash to show custom error messageif the error code was not 200
                flash('Thats not a Pokemon Try Again!!')
                return render_template("error.html")
                # return 'you typed something wrong!!!!'
            

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=2224)