import unittest

try:
    from .evaluation import evaluation_function
except ImportError:
    from evaluation import evaluation_function

model = 'gpt-3.5-turbo'
answer = 1

class TestEvaluationFunction(unittest.TestCase):
    """
        TestCase Class used to test the algorithm.
        ---
        Tests are used here to check that the algorithm written 
        is working as it should. 

        It's best practise to write these tests first to get a 
        kind of 'specification' for how your algorithm should 
        work, and you should run these tests before committing 
        your code to AWS.

        Read the docs on how to use unittest here:
        https://docs.python.org/3/library/unittest.html

        Use evaluation_function() to check your algorithm works 
        as it should.
    """

    def test_general_risk(self):
        response = "The pressurised vessel, because it could explode and cause injury if it's overpressurised."
        parameters = {'model': model, 'prompt':"The student needs to enter a risk with a short description of how it can cause harm"}
        output = evaluation_function(response, answer, parameters)
        self.assertEqual(output['is_correct'], True)

    def test_photosynthesis_definition_correct(self):
        response = "Photosynthesis is the process by which plants convert light energy into chemical energy to fuel their growth."
        parameters = {'model': model, 'prompt': "Evaluate the student's response for the definition of photosynthesis"}
        output = evaluation_function(response, answer, parameters)
        self.assertEqual(output["is_correct"], True)

    def test_photosynthesis_definition_incomplete(self):
        response = "Photosynthesis is the process by which plants make their food."
        parameters = {'model': model, 'prompt': "Evaluate the student's response for the definition of photosynthesis. They should mention the conversion of light energy to chemical energy."}
        output = evaluation_function(response, answer, parameters)
        self.assertEqual(output["is_correct"], False)

    def test_capital_city_incorrect(self):
        response = "The capital of France is Berlin."
        parameters = {'model': model, 'prompt': "Analyze the response regarding the capital of France"}
        output = evaluation_function(response, answer, parameters)
        self.assertEqual(output["is_correct"], False)

    def test_capital_city_partially_correct(self):
        response = "The capital of France is Paris, which is the largest city in the world."
        parameters = {'model': model, 'prompt': "Analyze the response regarding the capital of France"}
        output = evaluation_function(response, answer, parameters)
        self.assertEqual(output["is_correct"], False)

    def test_list(self):
        response = "Red, blue and yellow."
        parameters = {'model': model, 'prompt': "Mark this response asking students for the three primary colours in painting."}
        output = evaluation_function(response, answer, parameters)
        self.assertEqual(output["is_correct"], True)

    def test_physics_definition(self):
        response = "The law of conservation of energy states that energy cannot be created or destroyed, only transformed from one form to another. It's a fundamental principle in physics."
        parameters = {'model': model, 'prompt': "Examine the explanation of the law of conservation of energy and provide feedback."}
        output = evaluation_function(response, answer, parameters)
        self.assertEqual(output["is_correct"], True)

if __name__ == "__main__":
    unittest.main()