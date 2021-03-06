import unittest
from function import InputPreprocess

# Unit Test Case
  
class TestPenceEquivalent(unittest.TestCase):
    
    # Test function to test equality of two value
    def test_positive(self):

        # Test input dictionary "Key" represents User Input && "Value" represents Correct Answer
        user_input = {
            "6" : 6,
            "75": 75,
            "167p": 167, 
            "4p": 4, 
            "1.97": 197, 
            "£1.33": 133, 
            "£2": 200, 
            "£20": 2000, 
            "£1.97p": 197, 
            "£1p": 100, 
            "£1.p": 100, 
            "001.61p": 161, 
            "6.235p": 624, 
            "£1.256532677p": 126,
        }

        # Error message in case if test case got failed
        message = "First value and second value are not equal!"

        for key in user_input:

            input_amount = InputPreprocess(key)

            self.assertEqual(input_amount, user_input[key], message)

    # Test function for Error Inputs   
    def test_negative(self):

        user_input = ["", "1x", "£1x.0p", "£p", "asdasda"]
        ans = "This is an invalid input"

        # Error message in case if test case got failed
        message = "First value and second value are not equal!"

        for idx, val in enumerate (user_input):

            input_amount = InputPreprocess(val)

            self.assertEqual(input_amount, ans, message)

  
if __name__ == '__main__':
    unittest.main()