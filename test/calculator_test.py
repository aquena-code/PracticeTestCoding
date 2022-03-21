import unittest
from src.calculator import Calculator

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        cal = Calculator()
        result = cal.add(2, 2)
        self.assertEqual(4, result)

    def test_validate_age(self):
        cal = Calculator()
        result = cal.valid_age(5)
        self.assertTrue(result)

    def test_validate_invalid_age(self):
        cal = Calculator()
        result = cal.valid_age(-5)
        self.assertFalse(result)

# Test for Exercise 3
    def test_validate_maximun_numbers(self):
        cal = Calculator()
        result = cal.max_number(5, 2, 1)
        self.assertEqual(5, result)

    def test_validate_maximun_numbers_with_negatives(self):
        cal = Calculator()
        result = cal.max_number(-5, 2, -10)
        self.assertEqual(2, result)

#Test for Exercise 4
    def test_is_vocal(self):
        cal = Calculator()
        result = cal.is_vocal("A")
        self.assertEqual("vocal", result)

    def test_is_consonante(self):
        cal = Calculator()
        result = cal.is_vocal('b')
        self.assertEqual("consonante", result)

    def test_is_number(self):
        cal = Calculator()
        result = cal.is_vocal('2')
        self.assertEqual("number", result)