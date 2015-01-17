from webscraping import download, xpath

def getExternalRecipeUrl(url):
    dl = download.Download()
    html = dl.get(url)
    external_url = xpath.search(html, '//div[@class="external-directions flex-box"]//button/@link')
    actual_url = "http://www.yummly.com" + (external_url[0])
    return actual_url

def getSourceUrlFromYummlyUrl(url):
    dl = download.Download()
    html = dl.get(url)
    source_url = xpath.search(html, '//td[@class="close"]//a/@href')
    return source_url[0]

def getStepsFromSourceUrl(url):
    dl = download.Download()
    html = dl.get(url)
    steps = xpath.search(html, '//span[@class="recipePartStepDescription"]')
    return steps

def getStepsFromYummlyUrl(yummly_url):
    external_url = getExternalRecipeUrl(yummly_url)
    source_url = getSourceUrlFromYummlyUrl(external_url)
    steps = getStepsFromSourceUrl(source_url)
    return steps

def getUniqueSteps(steps):
    unique_steps = []
    for step in steps:
        if step not in unique_steps:
            unique_steps.append(step)
    return unique_steps
