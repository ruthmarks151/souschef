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
        intent = request.args.get('intent').encode('ascii','ignore')
        print "handling a request of",intent
        functions = {
            'query_temp': self.query_temp,
            'query_time': self.query_time,
            'convert_unit': self.parse_unit_conversion,
            'get_current_step': self.get_current_step,
            'next_step': self.next_step,
            'previous_step': self.previous_step,
            'ingredients': self.ingredients,
            'send_timer': self.send_time
        }

        return functions[intent](request)

    def relevant_time(self,request):
        pass
    def query_temp(self,request):
        return self.recipe.get_current_temp_text()
    def query_time(self,request):
        return self.recipe.get_current_time_text()
    def get_current_step(self,request):
        return self.recipe.get_current_step().get_step_text()
    def next_step(self,request):
        return self.recipe.next_step().get_step_text()

    def ingredients(self, request):
        return self.find_best_ingredient_amount(request.args.get('_text'))
    
    def find_best_ingredient_amount(self,phrase):
        words_in_phrase = phrase.split(" ")
        ingredients = self.recipe.get_ingredients()
        highest_matching = 0
        best_match = None
        for ingred in ingredients:
            matches = 0
            for i in ingred.get_raw().split(" "):
                for word in words_in_phrase:
                    if(word.lower() == i.lower()):
                        matches += 1
            if matches > highest_matching:
                highest_matching = matches
                best_match = ingred
        return "You need " + best_match.get_amount_string() + " " + best_match.get_unit() + " of " + best_match.get_name()

    def previous_step(self,request):
        return self.recipe.previous_step().get_step_text()

    def send_time(self, request):
        raw_statement = request.args.get('_text')
        words = raw_statement.split()
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

        milliseconds = Convert.convert_unit(numbers[0], units[0], "milliseconds")
        return "<" + str(milliseconds) + ">"

    def parse_unit_conversion(self, request):

        raw_statement = request.args.get('_text')
        words = raw_statement.split()
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

        final_string = str(numbers[0]) + " " + str(units[0]) + " is equal to " + str(Convert.convert_unit(numbers[0], units[0], units[1])) + " " + units[1]
        return final_string
