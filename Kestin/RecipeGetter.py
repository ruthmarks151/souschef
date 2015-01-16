import json, request

void searchForRecipe(searchTerms):
    r = requests.get('https://api.yummly.com', auth=('gofortks', 'souschef'))
