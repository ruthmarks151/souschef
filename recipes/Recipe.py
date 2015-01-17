#!/usr/bin/env python

class Recipe:
    def __init__(self, name, id, rating, ingredients, steps):
        self.steps = []
        self.ingredients = []
        self.current_step = 0
        for step in steps:
            if step is not '':
                self.steps.append(Step(step))

        for ingredient in ingredients:
            self.ingredients.append(ingredient)

    def get_recipe_name(self):
        return self.name

    def get_recipe_rating(self):
        return self.rating

    def get_recipe_total_time(self):
        return self.total_time

    def get_recipe_id(self):
        return self.id

    def get_current_step(self):
        return self.steps[self.current_step]

    def get_current_temp_text(self):
        return self.get_current_step().get_temp_text()

    def get_current_time_text(self):
        return self.get_current_step().get_time_text()

    def next_step(self):
        self.current_step += 1
        return self.get_current_step()

class Step:
    def __init__ (self,raw_text):
        self.text = raw_text
        self.temp_sentence = self.extract_temp_step(self.text)
        self.time_sentence = self.extract_time_step(self.text)
        self.ingredients = []

    def extract_temp_step(self,text):
        text = text.lower()
        sentences = text.split('.')
        degree_strings = ['degrees','deg',chr(248),'\xc2',' f ','fahrenheit',' c ','celcius','\xc2\xb0']
        for s in sentences:
            for w in degree_strings:
                if w in s:
                    return s

    def extract_time_step(self,text):
        text = text.lower()
        sentences = text.split('.')
        time_strings = ['minutes','minute','hour','hours','seconds']
        time_sentences = [s for s in sentences if any(word in s for word in time_strings)]
        for s in sentences:
            for w in time_sentences:
                if w in s:
                    return s

    def get_time_text(self):
        return self.time_sentence

    def get_temp_text(self):
        return self.temp_sentence


copied_text = """Preheat oven to 450degF. Place beef bones, carrots, leek, onion, and garlic on a roasting pan or rimmed baking sheet and roast for 20 minutes. Toss the contents of the pan and continue to roast until deeply browned, 10 to 20 minutes more.

Fill a large (at least 6-quart) stockpot with 12 cups of water (preferably filtered) . Add celery, bay leaves, peppercorns, and vinegar. Scrape the roasted bones and vegetables into the pot along with any juices. Add more water if necessary to cover bones and vegetables.

Cover the pot and bring to a gentle boil. Reduce heat to a very low simmer and cook with lid slightly ajar, skimming foam and excess fat occasionally, for at least 8 but up to 24 hours on the stovetop. The longer you simmer it, the better your stock will be. Add more water if necessary to ensure bone and vegetables are fully submerged. Alternately, you can cook the broth in a slow cooker on low for the same amount of time.

Remove the pot from the heat and let cool slightly. Strain broth using a fine-mesh sieve and discard bones and vegetables. Let continue to cool until barely warm, then refrigerate in smaller containers overnight. Remove solidified fat from the top of the chilled broth."""



#print(copied_text.split('\n'))
r = Recipe(copied_text.split('\n'),["pies"])
for i in range(10):
    print(r.get_current_temp_text())
    print(r.get_current_time_text())
    r.next_step()
