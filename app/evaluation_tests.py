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

    def test_compare_x_with_x(self):
        response, answer, params = "x", "x", dict()
        result = evaluation_function(
            response, answer, {"mode": "If they're the same, say it's correct. If they're different, say it's incorrect."})
        self.assertEqual(bool(result["result"]["is_correct"]), True)

    def test_compare_ketchup_and_red_sauce(self):
        response, answer, params = "ketchup", "red suace", dict()
        result = evaluation_function(
            response, answer, {"mode": "If they're the same, say it's correct. If they're different, say it's incorrect."})
        self.assertEqual(bool(result["result"]["is_correct"]), True)

    def test_compare_coal_and_red_sauce(self):
        response, answer, params = "green", "red suace", dict()
        result = evaluation_function(
            response, answer, {"mode": "If they're the same, say it's correct. If they're different, say it's incorrect."})
        self.assertEqual(bool(result["result"]["is_correct"]), False)


if __name__ == "__main__":
    unittest.main()
