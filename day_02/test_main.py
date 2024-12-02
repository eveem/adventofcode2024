import unittest
from main import read_input, diff_in_range, get_direction, is_safe, get_properties

class TestMain(unittest.TestCase):
    def test_read_input(self):
        filename = "small_input.txt"
        grid = read_input(filename)

        self.assertEqual(grid, [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]])
    
    def test_diff_in_range_true(self):
        self.assertEqual(diff_in_range([7, 6, 4, 2, 1], 1, 3), True)
    
    def test_diff_in_range_false(self):
        self.assertEqual(diff_in_range([1, 2, 7, 8, 9], 1, 3), False)
    
    def test_direction_inc(self):
        self.assertEqual(get_direction([1, 2, 7, 8, 9]), "inc")
    
    def test_direction_dec(self):
        self.assertEqual(get_direction([9, 7, 6, 2, 1]), "dec")
    
    def test_direction_tie(self):
        self.assertEqual(get_direction([8, 6, 4, 4, 1]), "tie")
    
    def test_direction_switch(self):
        self.assertEqual(get_direction([1, 3, 2, 4, 5]), "switch")
    
    def test_safe_row(self):
        self.assertEqual(is_safe([7, 6, 4, 2, 1], 1, 3), (True, "dec"))
    
    def test_unsafe_row_exceed_diff(self):
        self.assertEqual(is_safe([8, 4, 3, 2, 1], 1, 3), (False, "dec"))
    
    def test_unsafe_row_diff_less_than_lower_bound(self):
        self.assertEqual(is_safe([2, 4, 6, 8, 9], 2, 3), (False, "inc"))
    
    def test_unsafe_tie(self):
        self.assertEqual(is_safe([8, 6, 4, 4, 1], 1, 3), (False, "tie"))
    
    def test_unsafe_switch(self):
        self.assertEqual(is_safe([1, 3, 2, 4, 5], 1, 3), (False, "switch"))

    def test_get_properties_inc(self):
        self.assertEqual(get_properties([1, 2, 3, 4, 5]), (0, 4, 0))
    
    def test_get_properties_dec(self):
        self.assertEqual(get_properties([7, 6, 4, 2, 1]), (0, 0, 4))
    
    def test_get_properties_one_tie(self):
        self.assertEqual(get_properties([8, 6, 4, 4, 1]), (1, 0, 3))
    
    def test_get_properties_switch(self):
        self.assertEqual(get_properties([1, 3, 2, 4, 5]), (0, 3, 1))
    
    def test_get_properties_dec(self):
        self.assertEqual(get_properties([1, 3, 2, 4, 2]), (0, 2, 2))
