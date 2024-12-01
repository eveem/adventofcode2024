import unittest
from main import sort_sum_diff, read_input, count_freq, find_similarity_score

class TestMain(unittest.TestCase):
    def test_read_input(self):
        filename = "small_input.txt"
        nums1, nums2 = read_input(filename)

        self.assertEqual(nums1, [3, 4, 2, 1, 3, 3])
        self.assertEqual(nums2, [4, 3, 5, 3, 9 ,3])
    
    def test_sort_sum_diff(self):
        nums1 = [4, 3, 2]
        nums2 = [1, 3, 2]

        res = sort_sum_diff(nums1, nums2)
        self.assertEqual(res, 3)

    def test_count_freq(self):
        nums = [4, 3, 5, 3, 9, 3]
        self.assertEqual(count_freq(nums), {3: 3, 4: 1, 5: 1, 9: 1})
    
    def test_find_similarity_score(self):
        nums1 = [3, 4, 2, 1, 3, 3]
        nums2 = [4, 3, 5, 3, 9 ,3]

        self.assertEqual(find_similarity_score(nums1, nums2), 31)