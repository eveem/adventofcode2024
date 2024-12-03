import unittest
from main import read_input, extract_valid_mul, find_do_dont, format_pairs

class TestMain(unittest.TestCase):
    def test_read_small_input(self):
        filename = "1_small_input.txt"
        lines = read_input(filename)

        self.assertEqual(len(lines), 1)
    
    def test_read_small_input_single_quote(self):
        filename = "2_small_input.txt"
        lines = read_input(filename)

        self.assertEqual(len(lines), 1)

    def test_read_input(self):
        filename = "input.txt"
        lines = read_input(filename)

        self.assertEqual(len(lines), 6)
    
    def test_extract_valid_mul_simple(self):
        data = extract_valid_mul("xmul(2,4)%mul[3,7]^not_mul(5,5)")
        self.assertEqual(data, [[5, 5, 23], [2, 4, 1]])

    def test_extract_valid_mul_no_valid(self):
        data = extract_valid_mul("xmul(2,4]")
        self.assertEqual(data, [])

    def test_extract_valid_mul_complex(self):
        data = extract_valid_mul("mul(32,64]then(mul(11,8)mul(8,5))")
        self.assertEqual(data, [[8, 5, 24], [11, 8, 15]])

    def test_find_do_dont_with_index(self):
        data = find_do_dont("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
        self.assertEqual(data, {20: False, 59: True})

    def test_format_pairs(self):
        data = [[8, 5, 24], [11, 8, 15]]
        self.assertEqual(format_pairs(data), {24: [8, 5], 15: [11, 8]})