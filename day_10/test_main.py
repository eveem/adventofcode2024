import unittest
from main import read_input, dfs, find_start_points, count_path

class TestMain(unittest.TestCase):
    def test_read_small_input(self):
        filename = "small_input_01.txt"
        grid = read_input(filename)

        self.assertEqual(len(grid), 7)
        self.assertEqual(grid[0], "...0...")
    
    def test_dfs_small_input_1(self):
        grid = read_input("small_input_01.txt")
        expected = set()
        expected.add((6, 0))
        expected.add((6, 6))

        self.assertSetEqual(dfs(grid, 0, 3), expected)

    def test_dfs_small_input_2(self):
        grid = read_input("small_input_02.txt")
        expected = set()
        expected.add((6, 0))
        expected.add((0, 6))
        expected.add((1, 5))
        expected.add((4, 4))

        self.assertSetEqual(dfs(grid, 0, 3), expected)
    
    def test_dfs_small_input_3_1(self):
        grid = read_input("small_input_03.txt")
        expected = set()
        expected.add((5, 3))

        self.assertSetEqual(dfs(grid, 0, 1), expected)
    
    def test_dfs_small_input_3_2(self):
        grid = read_input("small_input_03.txt")
        expected = set()
        expected.add((5, 3))
        expected.add((0, 4))

        self.assertSetEqual(dfs(grid, 6, 5), expected)
    
    def test_find_start_points(self):
        grid = read_input("small_input_03.txt")
        expected = [[0, 1], [6, 5]]

        self.assertEqual(find_start_points(grid), expected)
    
    def test_count_path_small_input_5(self):
        grid = read_input("small_input_05.txt")
        expected = 3

        self.assertEqual(count_path(grid, 0, 5), expected)
    
    def test_count_path_small_input_6(self):
        grid = read_input("small_input_06.txt")
        expected = 227

        self.assertEqual(count_path(grid, 0, 0), expected)