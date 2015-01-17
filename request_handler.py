import sys
sys.path.insert(0, './recipes/')
import Recipe
import Convert
import json

class request_handler:

    def __init__(self,recipe):
        self.recipe = recipe

    def get_recipe(self):
        return self.recipe

    def handle_request(self,request):
        functions = {
            'query_temp': self.query_temp,
            'query_time': self.query_time,
            'convert_unit': self.convert_unit,
            'get_current_step': self.get_current_step,
            'next_step': self.next_step,
            'previous_step': self.previous_step,
            'ingredients': self.ingredient
        }

        return functions[request["intent"]](request)

    def query_temp(self,request):
        return self.recipe.get_current_temp_text()
    def query_time(self,request):
        return self.recipe.get_current_time_text()
    def convert_unit(self,request):
        parse_unit_converstion(request)
    def get_current_step(self,request):
        return self.recipe.get_current_step().get_step_text()
    def next_step(self,request):
        return self.recipe.get_next_step().get_step_text()
    def previous_step(self,request):
        return self.recipe.get_previous_step().get_step_text
    def ingredients(self, request):
        return find_best_ingredient_amount(request)


    def find_best_ingredient_amount(phrase):
        words_in_phrase = phrase.split()
        ingredients = recipe.get_ingredients()
        highest_matching = 0
        best_match = None
        for ingred in ingredients:
            matches = 0
            for i in ingred.getName().split():
                for word in words_in_phrase:
                    if(word.lower() == i.lower()):
                        matches += 1
            if matches > highest_matching:
                highest_matching = matches
                best_match = ingred
        return "You need " + ingred.get_amount_string() + " " + ingred.get_unts() + " of " + ingred.getName()

    def parse_unit_conversion(self, phrase):
        words = phrase.split()
        numbers = []
        units = []
        for i in range(len(words)):
            try:
                val = eval(words[i])
                if type(val) == int or type(val) == float:
                    numbers.append(val)
                    units.append(words[i + 1])
            except:
                if words[i] == 'to' or words[i] == 'in':
                    units.append(words[i + 1])
                continue

        final_string = str(numbers[0]) + " " + str(units[0]) + " is equal to " + str(Convert.convert_unit(numbers[0], units[0], units[1]))
        return final_string
