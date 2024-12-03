import unittest
from main import read_input, extract_valid_mul

class TestMain(unittest.TestCase):
    def test_read_small_input(self):
        filename = "1_small_input.txt"
        lines = read_input(filename)

        self.assertEqual(len(lines), 1)

    def test_read_input(self):
        filename = "input.txt"
        lines = read_input(filename)

        self.assertEqual(len(lines), 6)
    
    def test_extract_valid_mul_simple(self):
        data = extract_valid_mul("xmul(2,4)%mul[3,7]^not_mul(5,5)")
        self.assertEqual(data, [[2, 4], [5, 5]])

    def test_extract_valid_mul_no_valid(self):
        data = extract_valid_mul("xmul(2,4]")
        self.assertEqual(data, [])

    def test_extract_valid_mul_complex(self):
        data = extract_valid_mul("mul(32,64]then(mul(11,8)mul(8,5))")
        self.assertEqual(data, [[11, 8], [8, 5]])