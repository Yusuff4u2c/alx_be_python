import unittest 
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Create an instance of SimpleCalculator before each test."""
        self.calc= SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtraction(5, 3), 2)
        self.assertEqual(self.calc.subtraction(3, 5), -2)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 5), -5)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, 0), None)  # Division by zero
        self.assertEqual(self.calc.divide(0, 5), 0)      # Zero numerator