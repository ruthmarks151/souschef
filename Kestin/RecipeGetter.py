from yummly import Client

# default option values
TIMEOUT = 5.0
RETRIES = 0

client = Client(api_id = '0ad05d37', api_key = 'b616f863887a7d2cb6d4baf30cd3cbe2', timeout = TIMEOUT, retries = RETRIES)

def searchForRecipe(search_terms):
    search = client.search(search_terms)
    return search.matches[0]

def getRecipeInfo(recipeId):
    recipe = client.recipe(recipeId)
