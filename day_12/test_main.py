import unittest
from main import read_input, find_perimeter

class TestMain(unittest.TestCase):
    def test_read_small_input(self):
        filename = "small_input_01.txt"
        grid = read_input(filename)

        self.assertEqual(len(grid), 4)
        self.assertEqual(grid[0], "AAAA")
    
    def test_dfs_small_input_1(self):
        grid = read_input("small_input_01.txt")
        expected_area = 4
        expected_perimeter = 10
        expected_seen = {(0, 0), (0, 1), (0, 2), (0, 3)}

        result_area, result_perimeter, result_seen = find_perimeter(grid, "A", 0, 0, set())

        self.assertEqual(result_area, expected_area)
        self.assertEqual(result_perimeter, expected_perimeter)
        self.assertEqual(result_seen, expected_seen)
    
    def test_dfs_small_input_2(self):
        grid = read_input("small_input_02.txt")
        expected_area_x = 1
        expected_perimeter_x = 4
        expected_seen_x = {(1, 1)}

        result_area_x, result_perimeter_x, result_seen_x = find_perimeter(grid, "X", 1, 1, set())

        expected_area_o = 21
        expected_perimeter_o = 36
        expected_seen_o = {
            (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 2), (1, 4),
            (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 2), (3, 4),
            (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (1, 1)
        }
        result_area_o, result_perimeter_o, result_seen_o = find_perimeter(grid, "O", 0, 0, {(1, 1)})

        self.assertEqual(result_area_x, expected_area_x)
        self.assertEqual(result_perimeter_x, expected_perimeter_x)
        self.assertSetEqual(result_seen_x, expected_seen_x)

        self.assertEqual(result_area_o, expected_area_o)
        self.assertEqual(result_perimeter_o, expected_perimeter_o)
        self.assertSetEqual(result_seen_o, expected_seen_o)