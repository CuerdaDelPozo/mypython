import unittest

from app.routes import pum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        result = pum(data)
        self.assertEqual(result, 6)

    def test_with_tupple(self):
        data = (1, 2, 3, 4)
        result = pum(data)
        self.assertEqual(result, 24)

    def test_fail_with_string(self):
        data = [1, 2, '3', '4', '5']
        result = pum(data)
        self.assertEqual(result[0], "Error occured!") 
        self.assertEqual(result[1], 500) 

    def test_fail_with_single_value(self):
        data = 1
        result = pum(data)
        self.assertEqual(result[0], "Error occured!") 
        self.assertEqual(result[1], 500) 
