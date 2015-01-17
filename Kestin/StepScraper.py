from lxml import html
import requests

def getStepsFromUrl(url):
    page = requests.get(url)
    tree = html.fromstring(page.text)
    steps = tree.xpath('//span[@class="recipePartStepDescription"]/text()')
    print("===")
    print(steps)

getStepsFromUrl('http://www.yummly.com/recipe/external/Bacon-Cheddar-Pinwheels-768341')
