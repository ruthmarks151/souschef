from flask import Flask, request
import sys
import os
from request_handler import request_handler
sys.path.insert(0, './recipes/')
import RecipeGetter

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

def create_recipe(search):
    return request_handler(RecipeGetter.getRecipe(search))

rh = create_recipe("bacon")

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/static/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(os.path.join('static', path))

if __name__ == '__main__':  # pragma: no cover
    app.run(host='0.0.0.0', port=5001)
