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

#Test for Exercise 5

    def test_reverse(self):
        cal = Calculator()
        result = cal.reverse("Cadena")
        self.assertEqual("anedaC", result)

#Test for Exercise 6

    def test_palindromo(self):
        cal = Calculator()
        result = cal.is_palindromo("rayar")
        self.assertTrue(result)

#Test for Exercise 7

    def test_max_min_average_result(self):
        numbers = [3, 4, 5, 3, 2, 3, 5, 6, 5, 1]
        result = Resultado()
        cal = Calculator()
        result = cal.get_results()
        self.assertEqual(1, result.min_number)
        self.assertEqual(6, result.max_number)
        self.assertEqual(3.7, result.average)

#Test for Exercise 8

    def test_longer_country(self):
        countries = ['Bolivia', 'Argentina', 'Colombia', 'Italia', 'Japon']
        cal = Calculator()
        result = cal.get_longer_country(countries)
        self.assertEqual("Argentina", result)

#Test for Exercise 10

    def test_counter_characters(self):
        cal = Calculator()
        result = cal.count_characters("this chain is very large")
        self.assertEqual(20, result)

