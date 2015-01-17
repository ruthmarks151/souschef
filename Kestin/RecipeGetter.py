from yummly import Client
import StepScraper

TIMEOUT = 5.0
RETRIES = 0

client = Client(api_id = '0ad05d37', api_key = 'b616f863887a7d2cb6d4baf30cd3cbe2', timeout = TIMEOUT, retries = RETRIES)

def getFirstRecipeIdFromSearch(search_terms):
    results = client.search(search_terms)
    match = results.matches[0]
    return match.id

def listRecipesFromSearch(search_terms):
    results = client.search(search_terms, maxResults=1)

    print 'Total Matches:', results.totalMatchCount
    for match in results.matches:
        try:
            print 'Recipe ID:', match.id
            print 'Recipe:', match.recipeName
            print 'Rating:', match.rating
            print 'Total Time (mins):', (match.totalTimeInSeconds / 60.0)
            print '----------------------------------------------------'
        except:
            print '==ERROR=='

def getRecipeInfo(recipe_id):
    return client.recipe(recipe_id)

def printRecipeInfo(recipe):
    print ""
    print 'Recipe ID:', recipe.id
    print 'Recipe:', recipe.name
    print 'Rating:', recipe.rating
    print 'Total Time:', recipe.totalTime
    print 'Yields:', recipe.yields
    print 'Ingredients:'
    for ingred in recipe.ingredientLines:
        print ingred
    print ""

def getSourceFromRecipe(recipe):
    url = recipe.source.sourceRecipeUrl
    return url

a = getFirstRecipeIdFromSearch('bacon')
b = getRecipeInfo(a)
c = getSourceFromRecipe(b)
d = StepScraper.getStepsFromYummlyUrl(c)
e = StepScraper.getUniqueSteps(d)
print e
printRecipeInfo(b)
