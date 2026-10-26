import unittest

from Calc import Calculator  # The class we are going to implement


class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5

    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(5, 3)
        self.assertEqual(result, 2)  # Expect 5 - 3 = 2

    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(2, 3)
        self.assertEqual(result, 6)  # Expect 2 * 3 = 6

    def test_divide(self):
        calc = Calculator()
        result = calc.divide(6, 3)
        self.assertEqual(result, 2)  # Expect 6 / 3 = 2

    def test_divide_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ZeroDivisionError):
            calc.divide(6, 0)  # Expect division by zero to raise an error

    def test_modulo(self):
        calc = Calculator()
        result = calc.modulo(7, 3)
        self.assertEqual(result, 1)  # Expect 7 % 3 = 1

    def test_modulo_negative_dividend(self):
        calc = Calculator()
        result = calc.modulo(-7, 3)
        # Remainder takes the sign of the dividend (truncated division, as in C/Java)
        self.assertEqual(result, -1)

    def test_modulo_negative_divisor(self):
        calc = Calculator()
        result = calc.modulo(7, -3)
        # Truncated semantics: the divisor's sign is ignored, the dividend's is kept
        self.assertEqual(result, 1)

    def test_modulo_by_zero(self):
        calc = Calculator()
        # Same error and message as divide() for a zero divisor
        with self.assertRaisesRegex(ZeroDivisionError, "Cannot divide by zero"):
            calc.modulo(7, 0)

    def test_power(self):
        calc = Calculator()
        result = calc.power(2, 3)
        self.assertEqual(result, 8)  # Expect 2 ** 3 = 8

    def test_power_zero_to_zero(self):
        calc = Calculator()
        result = calc.power(0, 0)
        self.assertEqual(result, 1)  # Convention: 0 ** 0 = 1

    def test_power_negative_exponent(self):
        calc = Calculator()
        result = calc.power(2, -1)
        self.assertEqual(result, 0.5)  # Expect 2 ** -1 = 1 / 2 = 0.5

    def test_power_zero_to_negative_exponent(self):
        calc = Calculator()
        # Same error and message as divide() and modulo()
        with self.assertRaisesRegex(ZeroDivisionError, "Cannot divide by zero"):
            calc.power(0, -1)


if __name__ == "__main__":
    unittest.main()
