from django.test import TestCase

from app.calc import add
from app.calc import subtract


class CalcTests(TestCase):
    
    def test_add_numbers(self):
        """ Test that two numbers are added together"""
        self.assertEqual(add(3, 4), 7)

    def test_subtract_numbers(self):
        """Test that values are subtract and return"""
        self.assertEqual(subtract(5, 10), 5)