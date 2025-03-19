import unittest
from main import app

class TestCalculateEndpoint(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_calculate(self):
        # Define the input data
        input_data = {
            "test": {
            "input1": "5",
            "input2": "6"
            }
        }
        
        # Send a POST request to the /calculate endpoint
        response = self.app.post('/calculate', json=input_data)
        
        # Assert the response status code
        self.assertEqual(response.status_code, 200)
        
        # Assert the response data
        # expected_result = sum(ord(char) for char in 'test')
        expected_result = 11
        print(response.get_json())
        self.assertEqual(response.get_json(), {'result': expected_result})

if __name__ == '__main__':
    unittest.main()