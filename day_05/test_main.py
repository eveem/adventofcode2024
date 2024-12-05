import unittest
from main import read_input, is_correct_order, invalid_pairs, permutation, count_freq

class TestMain(unittest.TestCase):
    def test_read_small_input(self):
        filename = "test_input.txt"
        valid, order = read_input(filename)

        self.assertTrue((75, 47) in valid)
        self.assertTrue((47, 61) in valid)
        self.assertEqual(order, [
            [75, 47, 61, 53, 29], 
            [97, 61, 53, 29, 13],
            [75, 29, 13]
        ])
    
    def test_is_correct_order_true(self):
        valid = set([(75, 29), (75, 13), (29, 13)])
        order = [75, 29, 13]

        self.assertTrue(is_correct_order(valid, order))
    
    def test_is_correct_order_false(self):
        valid = set([(75, 29), (13, 75), (29, 13)])
        order = [75, 29, 13]

        self.assertFalse(is_correct_order(valid, order))
    
    def test_invalid_pairs(self):
        valid = set([
            (97, 75), (97, 47), (97, 29), 
            (97, 13), (75, 47), (75, 29), 
            (75, 13), (47, 29), (47, 13), 
            (29, 13)
        ])
        order = [97, 13, 75, 29, 47]

        self.assertEqual(invalid_pairs(valid, order), [
            [13, 75], [13, 29], [13, 47], [29, 47]
        ])
    
    def test_permutation(self):
        nums = [97, 13, 75]
        self.assertEqual(permutation(nums), [
            [97, 13, 75],
            [97, 75, 13],
            [13, 97, 75],
            [13, 75, 97],
            [75, 97, 13],
            [75, 13, 97]
        ])
    
    def test_count_freq(self):
        valid = set([
            (97, 75), (97, 47), (97, 29), 
            (97, 13), (75, 47), (75, 29), 
            (75, 13), (47, 29), (47, 13), 
            (29, 13)
        ])
        order = [97, 13, 75, 29, 47]
        res = count_freq(valid, order)
        self.assertDictEqual(res, {
            97: 4, 75: 3,
            47: 2, 29: 1
        })
