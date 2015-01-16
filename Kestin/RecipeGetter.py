import json, request

def searchForRecipe(searchTerms):
    r = requests.get('https://api.yummly.com', auth=('gofortks', 'souschef'))
