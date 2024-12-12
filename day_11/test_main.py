import unittest
from main import read_input, blink
from collections import Counter

class TestMain(unittest.TestCase):
    def test_read_small_input(self):
        filename = "small_input_02.txt"
        stones = read_input(filename)
        expected = Counter(["125", "17"])

        self.assertDictEqual(stones, expected)
    
    def test_blink(self):
        stones = Counter(["125", "17"])
        expected = Counter(["253000", "1", "7"])

        self.assertDictEqual(blink(stones), expected)
    
    def test_blink_bigger(self):
        stones = Counter(["0", "1", "10", "99", "999"])
        expected = Counter(["1", "2024", "1", "0", "9", "9", "2021976"])

        self.assertDictEqual(blink(stones), expected)