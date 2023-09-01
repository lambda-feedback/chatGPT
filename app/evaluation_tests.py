import unittest

try:
    from .evaluation import evaluation_function
except ImportError:
    from evaluation import evaluation_function

model = 'gpt-3.5-turbo'

default_prompt = "Output a Boolean: True if the student is correct and False if the student is incorrect"

answer = 1

class TestEvaluationFunction(unittest.TestCase):

    def test_general_risk(self):
        response = "The pressurised vessel, because it could explode and cause injury if it's overpressurised."
        parameters = {'model': model, 
                      'main_prompt': "The student needs to enter a risk with a short description of how it can cause harm",
                      'feedback_prompt': "You are an AI who should provide objective and constructive feedback to the student",
                      'default_prompt': default_prompt}
        output = evaluation_function(response, answer, parameters)
        self.assertEqual(output['is_correct'], True)

    def test_photosynthesis_definition_correct(self):
        response = "Photosynthesis is the process by which plants convert light energy into chemical energy to fuel their growth."
        parameters = {'model': model, 
                      'main_prompt': "Evaluate the student's response for the definition of photosynthesis",
                      'feedback_prompt': "You are an AI who should provide objective and constructive feedback to the student",
                      'default_prompt': default_prompt}
        output = evaluation_function(response, answer, parameters)
        self.assertEqual(output["is_correct"], True)

    def test_photosynthesis_definition_incomplete(self):
        response = "Photosynthesis is the process by which plants make their food."
        parameters = {'model': model, 
                      'main_prompt': "Evaluate the student's response for the definition of photosynthesis. They should mention the conversion of light energy to chemical energy.",
                      'feedback_prompt': "You are an AI who should provide objective and constructive feedback to the student",
                      'default_prompt': default_prompt}
        output = evaluation_function(response, answer, parameters)
        self.assertEqual(output["is_correct"], False)

    def test_capital_city_incorrect(self):
        response = "The capital of France is Berlin."
        parameters = {'model': model, 
                      'main_prompt': "Analyze the response regarding the capital of France",
                      'feedback_prompt': "You are an AI who should provide objective and constructive feedback to the student",
                      'default_prompt': default_prompt}
        output = evaluation_function(response, answer, parameters)
        self.assertEqual(output["is_correct"], False)

    def test_list(self):
        response = "Red, blue and yellow."
        parameters = {'model': model, 
                      'main_prompt': "Mark this response asking students for the three primary colours in painting.",
                      'feedback_prompt': "You are an AI who should provide objective and constructive feedback to the student",
                      'default_prompt': default_prompt}
        output = evaluation_function(response, answer, parameters)
        self.assertEqual(output["is_correct"], True)

    def test_physics_definition(self):
        response = "The law of conservation of energy states that energy cannot be created or destroyed, only transformed from one form to another. It's a fundamental principle in physics."
        parameters = {'model': model, 
                      'main_prompt': "Examine the explanation of the law of conservation of energy and provide feedback.",
                      'feedback_prompt': "You are an AI who should provide objective and constructive feedback to the student",
                      'default_prompt': default_prompt}
        output = evaluation_function(response, answer, parameters)
        self.assertEqual(output["is_correct"], True)

if __name__ == "__main__":
    unittest.main()
