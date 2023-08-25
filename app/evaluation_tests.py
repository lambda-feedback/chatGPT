import unittest

try:
    from .evaluation import evaluation_function
except ImportError:
    from evaluation import evaluation_function

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

    def test_risk(self):
        prompt = "The student needs to enter a risk with a short description of how it can cause harm"
        response = "The sun becuase UV rays can cause damage"
        parameters = {'model': 'gpt-3.5-turbo-16k'}
        output = evaluation_function(response, prompt, parameters)
        self.assertEqual(output["is_correct"], True)

if __name__ == "__main__":
    unittest.main()
