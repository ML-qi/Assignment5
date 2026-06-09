import unittest
from Assignment5 import calculate, fibonacci

class TestCalculate(unittest.TestCase):
    def test_calculate_valid_input(self):
        self.assertAlmostEqual(calculate(32), 0.0)
        self.assertAlmostEqual(calculate(212), 100.0)
        self.assertAlmostEqual(calculate(98.6), 37.0)

    def test_calculate_invalid_input(self):
        with self.assertRaises(TypeError):
            calculate("not a number")
        with self.assertRaises(TypeError):
            calculate(None)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        
    def test_fibonacci_invalid_input(self):
        with self.assertRaises(TypeError):
            fibonacci("1.5")
        with self.assertRaises(ValueError):
            fibonacci(-1)
if __name__ == '__main__':    
    unittest.main()
