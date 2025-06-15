import unittest 
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Create an instance of SimpleCalculator before each test."""
        self.calculator = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)

    def test_subtract(self):
        """Test the subtraction method."""
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(3, 5), -2)

    def test_multiply(self):
        """Test the multiplication method."""
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-1, 5), -5)

    def test_divide(self):
        """Test the division method."""
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertEqual(self.calculator.divide(5, 0), None)  # Division by zero
        self.assertEqual(self.calculator.divide(0, 5), 0)      # Zero numerator