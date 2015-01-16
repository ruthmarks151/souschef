from yummly import Client

# default option values
TIMEOUT = 5.0
RETRIES = 0

client = Client(api_id = '0ad05d37', api_key = 'b616f863887a7d2cb6d4baf30cd3cbe2', timeout = TIMEOUT, retries = RETRIES)

def getFirstRecipeIdFromSearch(search_terms):
    search = client.search(search_terms)
    return search.matches[0].id

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

def getRecipeInfo(recipeId):
    recipe = client.recipe(recipeId)

listRecipesFromSearch("bacon")
