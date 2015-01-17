#!/usr/bin/env python

class Recipe:
    def __init__(self, name, recipe_id, rating, ingredients, steps, picture_url):
        self.name = name
        self.recipe_id = recipe_id
        self.rating = rating
        self.ingredients = []
        self.steps = []
        self.picture_url = picture_url
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

    def get_recipe_id(self):
        return self.recipe_id

    def get_current_step(self):
        return self.steps[self.current_step]

    def get_picture_url(self):
        return self.picture_url

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

    def get_step_text(self):
        return self.text

class Ingredient:
    def __init__(self, raw_text):
        text = raw_text.split();
        amount = []
        for word in text:
            try:
                if type(eval(word)) == int:
                    amount.append(word);
            except:
                break
        self.unit = text[len(amount)]
        for i in range(len(amount) + 1):
            del text[0]
        self.name = ' '.join(text)
        self.amount = amount

    def get_name(self):
        return self.name

    def get_amount_number(self):
        total = 0
        for i in self.amount:
            total += eval(i + ".0")
        return total

    def get_amount_string(self):
        return ' '.join(self.amount)

    def get_unit(self):
        return self.unit
