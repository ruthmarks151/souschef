from flask import Flask, request, jsonify
import sys
import os
import urllib
from request_handler import request_handler
sys.path.insert(0, './recipes/')
import RecipeGetter
import json
import postmates

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')
rh = None

@app.route('/recipe/get/first/<search>')
def create_recipe(search):
    return jsonify(results=RecipeGetter.getRecipe(search))

@app.route('/say/<phrase>')
def say(phrase):
    phrase = phrase.encode('ascii','ignore')
    try:
        os.system('say "'+urllib.unquote(phrase)+'"')
    except:
        pass

    return "200"

@app.route('/recipe/<recipe_id>')
def choose_recipe(recipe_id):
    global rh
    recipe_id = recipe_id.encode('ascii','ignore')
    r = RecipeGetter.getRecipeClassFromId(recipe_id)
    rh = request_handler(r)
    return jsonify(results=RecipeGetter.getRecipeFromId(recipe_id))

@app.route('/recipe/get/all/<search>')
def return_all_recipes(search):
    print 'looking for',search
    return jsonify(results=RecipeGetter.getAllUseableRecipes(search))

@app.route('/functions')
def return_speech():
    print "request gotten!"
    global rh
    response = rh.handle_request(request)
    print response
    return str(response)

@app.route('/postmates/get/quote')
def get_postmates_quote():
    pickup_addr = request.args.get("pickup_address")
    dropoff_addr = request.args.get("dropoff_address")
    result = postmates.post_delivery_quote(pickup_addr, dropoff_addr)
    return result.json()['id']

@app.route('/postmates/create/order')
def create_postamtes_order():
    ingreds = rh.recipe.get_ingredients_raw();
    order = ""
    for ingred in ingreds:
        order += " " + ingred

    params = {
        'manifest': "" + order,
        'pickup_name': "" ,
        'pickup_address': "" + request.args.get("pickup_address"),
        'pickup_phone_number': "" + request.args.get("pickup_phone_number"),
        'pickup_business_name': "" + request.args.get("pickup_business_name"),
        'pickup_notes': "" + request.args.get("pickup_notes"),
        'dropoff_name': "" + request.args.get("dropoff_name"),
        'dropoff_address': "" + request.args.get("dropoff_address"),
        'dropoff_phone_number': "" + request.args.get("dropoff_phone_number"),
        'dropoff_business_name': "",
        'dropoff_notes': "" + request.args.get("dropoff_notes"),
        'quote_id': request.args.get("quote_id"),
    }
    result = postmates.post_create_delivery(params)
    j = result.json()
    return "200"


@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/static/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(os.path.join('static', path))

@app.route('/request/ingredients/')
def request_ingredients():
    return jsonify(results=rh.get_recipe().get_ingredients_raw())

if __name__ == '__main__':  # pragma: no cover
    app.run(host='0.0.0.0', port=5001, debug = True)
