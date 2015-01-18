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
def create_recipe(phrase):
    urllib.unquote(phrase)
    os.system("say "+'"urllib.unquote(phrase)"')

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
    print pickup_addr
    print dropoff_addr
    return postmates.post_delivery_quote(pickup_addr, dropoff_addr).json()

@app.route('/postmates/create/delivery')
def create_postamtes_order():
    return postmates.post_create_delivery()


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
