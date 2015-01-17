from yummly import Client
import StepScraper

TIMEOUT = 5.0
RETRIES = 0

client = Client(api_id = '0ad05d37', api_key = 'b616f863887a7d2cb6d4baf30cd3cbe2', timeout = TIMEOUT, retries = RETRIES)

allowed_recipe_sources = ["Pillsbury Brand", "Betty Crocker", "Tablespoon"]
def getFirstUseableRecipeId(params):
    results = client.search(**params)
    matches = results.matches
    for match in matches:
        if match.sourceDisplayName in allowed_recipe_sources:
        return match

def getRecipeFromId(id):
    return client.recipe(id)

def getSourceFromRecipe(recipe):
    url = recipe.source.sourceRecipeUrl
    return url

search_params = {
    'q': "bacon",
    'start': 0,
    'maxResults': 100,
    'requirePicutres': True
}

def getSteps():
    return 4
