from flask import Flask, request, jsonify
import sys
import os
from request_handler import request_handler
sys.path.insert(0, './recipes/')
import RecipeGetter
import json

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')
rh = None

@app.route('/recipe/get/first/<search>')
def create_recipe(search):
    return jsonify(results=RecipeGetter.getRecipe(search))

@app.route('/recipe/choose/<recipe_id>')
def choose_recipe(recipe_id):
    global rh
    recipe_id = recipe_id.encode('ascii','ignore')
    r = RecipeGetter.getRecipeClassFromId(recipe_id)
    rh = request_handler(r)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

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
