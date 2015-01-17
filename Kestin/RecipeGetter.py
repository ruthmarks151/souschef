from yummly import Client
import StepScraper

TIMEOUT = 5.0
RETRIES = 0

client = Client(api_id = '0ad05d37', api_key = 'b616f863887a7d2cb6d4baf30cd3cbe2', timeout = TIMEOUT, retries = RETRIES)

def getFirstRecipeIdFromSearch(search_params):
    results = client.search(**search_params)
    match = results.matches[0]
    print match
    return match.id

def getFirstUseableRecipeId(params):
    results = client.search(**params)
    matches = results.matches
    for match in matches:
        if match.sourceDisplayName in allowed_source:
        return match

def getRecipeFromId(id):
    return client.recipe(id)

allowed_source = ["Pillsbury Brand", "Betty Crocker", "Tablespoon"]

def getSourceFromRecipe(recipe):
    url = recipe.source.sourceRecipeUrl
    return url

params = {
    'q': "bacon",
    'start': 0,
    'maxResults': 100,
    'requirePicutres': True
}
