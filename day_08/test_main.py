import unittest
from main import read_input, list_position, find_diff, generate_antinode

class TestMain(unittest.TestCase):
    def test_read_small_input(self):
        filename = "small_input.txt"
        grid = read_input(filename)

        self.assertEqual(len(grid), 12)
    
    def test_list_position(self):
        grid = [
            list(".........."),
            list(".........."),
            list(".........."),
            list("....a....."),
            list(".........."),
            list(".....a...."),
            list(".........."),
            list(".........."),
            list(".........."),
            list("..........")
        ]

        self.assertDictEqual(list_position(grid), {"a": [[3, 4], [5, 5]]})
    
    def test_find_diff(self):
        points = [[3, 4], [5, 5], [4, 8]]

        self.assertListEqual(find_diff(points), [[2, 1], [1, 4], [-1, 3]])
    
    def test_generate_antinode(self):
        points = [[3, 4], [5, 5], [4, 8]]
        antinodes = generate_antinode(points, 10, 10, False)

        self.assertTrue([1, 3] in antinodes)
        self.assertTrue([2, 0] in antinodes)
        self.assertTrue([6, 2] in antinodes)
        self.assertTrue([7, 6] in antinodes)
    
    def test_generate_antinode_multiple_points(self):
        points = [[0, 0], [1, 3], [2, 1]]
        antinodes = generate_antinode(points, 10, 10, True)

        self.assertTrue([0, 5] in antinodes)
        self.assertTrue([2, 6] in antinodes)
        self.assertTrue([3, 9] in antinodes)
        self.assertTrue([4, 2] in antinodes)
        self.assertTrue([6, 3] in antinodes)
        self.assertTrue([8, 4] in antinodes)