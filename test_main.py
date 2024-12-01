import unittest
from main import sort_sum_diff, read_input

class TestMain(unittest.TestCase):
    def test_read_input(self):
        filename = "small_input.txt"
        nums1, nums2 = read_input(filename)

        self.assertEqual(nums1, [3, 4, 2, 1, 3, 3])
        self.assertEqual(nums2, [4, 3, 5, 3, 9 ,3])