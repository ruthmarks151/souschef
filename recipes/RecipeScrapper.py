from webscraping import download, xpath

#
# This would work if the webpage didn't render the html with js. So It's broken.
#

def getTopRecipes(search_terms):
    url = "http://www.tablespoon.com/search?term=" + (search_terms.replace(' ', '%20'))
    dl = download.Download()
    html = dl.get(url)
    names = xpath.search(html, '//div[@class="li-text"]//a/@text')
    print html
    imgs = xpath.search(html, '//div[@data-bind="attr: { \'data-src\': StandardImages.GridViewImageUrl, \'data-media\': $root.MediaQueryLarge }"]/@data-src')
    ratings = xpath.search(html, '//span[@data-bind=" attr: { \'title\': AdditionalInfo.RatingDescription, \'class\': AdditionalInfo.RatingCssClassName }"]/@title')
    recipe_links = xpath.search(html, '//div[@class="li-text"]//a/@href')

    recipes = []
    print len(imgs)

    for i in range(len(names)):
        url = "http://www.tablespoon.com" + recipe_links[i]
        html = dl.get(url)

        extra_info = xpath.search(html, '//div[@class="recipePartAttributes recipePartPrimaryAttributes"]//ul//li//span/@text')

        ingredients_amount = xpath.search(html, '//dl[@class="recipePartIngredient"]//dt//span/@text')
        ingredients_words = xpath.search(html, '//dl[@class="recipePartIngredient"]//dd//span/@text')

        ingredient = ingredient_amount[0] + " " + ingredient_words[0]

        steps = xpath.search(html, '//span[@class="recipePartStepDescription"]')
        unique_steps = []
        for step in steps:
            if step not in unique_steps:
                unique_steps.append(step)

        recipes.append(Recipe(names[i], eval(ratings[i].split()[0]), imgs[i], ingredients, unique_steps, extra_info[0], extra_info[1], extra_info[2]))

    return recipes

recipes = getTopRecipes("beef")
print recipes

class Recipe:
    def __init__(self, name, rating, img_url, ingredients, steps, prep_time, total_time, servings):
        self.name = name
        self.rating = rating
        self.prep_time = prep_time
        self.total_time = total_time
        self.servings = servings
        self.ingredients = []
        self.steps = []
        self.img_url = img_url
        self.current_step = 0
        for step in steps:
            if step is not '':
                self.steps.append(Step(step))

        for ingredient in ingredients:
            self.ingredients.append(Ingredient(ingredient))

    def get_recipe_name(self):
        return self.name

    def get_recipe_rating(self):
        return self.rating

    def get_recipe_total_time(self):
        return self.total_time

    def get_recipe_prep_time(self):
        return self.prep_time

    def get_recipe_Servings(self):
        return self.servings

    def get_current_step(self):
        return self.steps[self.current_step]

    def get_img_url(self):
        return self.img_url

    def get_ingredients_raw(self):
        return self.ingredients

    def get_current_temp_text(self):
        return self.get_current_step().get_temp_text()

    def get_current_time_text(self):
        return self.get_current_step().get_time_text()

    def next_step(self):
        self.current_step += 1
        return self.get_current_step()

    def previous_step(self):
        if self.current_step > 0:
            self.current_step -= 1
        return self.get_current_step()
