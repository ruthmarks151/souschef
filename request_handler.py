import sys
sys.path.insert(0, './recipes/')
import Recipe
import Convert
import json

class request_handler:

    def __init__(self,recipe):
        self.recipe = recipe

    def handle_request(self,request):
        functions = {
            'query_temp': self.query_temp,
            'query_time': self.query_time,
            'convert_unit': self.convert_unit,
            'send_timer': self.send_timer,
            'get_current_step': self.get_current_step,
            'next_step': self.next_step,
            'previous_step': self.previous_step,
            'ingredients': self.ingredients
        }

        return functions[request["intent"]](request)

    def query_temp(self,request):
        return self.recipe.get_current_temp_text()
    def query_time(self,request):
        return self.recipe.get_current_time_text()
    def convert_unit(self,request):
        pass
    def send_timer(self,request):
        pass
    def get_current_step(self,request):
        return self.recipe.get_current_step().get_step_text()
    def next_step(self,request):
        return self.recipe.get_next_step().get_step_text()
    def previous_step(self,request):
        return self.recipe.get_previous_step().get_step_text()
    def ingredients(self,request):
        return json.dumps(self.recipe.get_ingredients())
