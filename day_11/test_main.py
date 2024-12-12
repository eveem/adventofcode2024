import unittest
from main import read_input, blink, calculate
from collections import Counter

class TestMain(unittest.TestCase):
    def test_read_small_input(self):
        filename = "small_input_02.txt"
        stones = read_input(filename)

        self.assertEqual(stones, ["125", "17"])
    
    def test_blink_zero(self):
        stone = "0"
        expected = ["1"]

        self.assertEqual(blink(stone), expected)
    
    def test_blink_even_digit(self):
        stone = "99"
        expected = ["9", "9"]

        self.assertEqual(blink(stone), expected)
    
    def test_blink_even_digit_zero_leading_10(self):
        stone = "10"
        expected = ["1", "0"]

        self.assertEqual(blink(stone), expected)
    
    def test_blink_even_digit_zero_leading_1000(self):
        stone = "1000"
        expected = ["10", "0"]

        self.assertEqual(blink(stone), expected)
    
    def test_blink_no_rule_apply_1(self):
        stone = "1"
        expected = ["2024"]

        self.assertEqual(blink(stone), expected)
    
    def test_blink_no_rule_apply_2024(self):
        stone = "999"
        expected = ["2021976"]

        self.assertEqual(blink(stone), expected)
    
    def test_calculate(self):
        stones = ["0", "1", "10", "99", "999"]
        expected = ["1", "2024", "1", "0", "9", "9", "2021976"]

        self.assertEqual(calculate(stones), expected)