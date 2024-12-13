import unittest
from collections import Counter
from main import read_input, find_perimeter, find_corners, flood_field

class TestMain(unittest.TestCase):
    def test_read_small_input(self):
        filename = "small_input_01.txt"
        grid = read_input(filename)

        self.assertEqual(len(grid), 4)
        self.assertEqual(grid[0], "AAAA")
    
    def test_find_perimeter_small_input_1(self):
        grid = read_input("small_input_01.txt")
        expected_area = 4
        expected_perimeter = 10
        expected_seen = {(0, 0), (0, 1), (0, 2), (0, 3)}

        result_area, result_perimeter, result_seen = find_perimeter(grid, "A", 0, 0, set())

        self.assertEqual(result_area, expected_area)
        self.assertEqual(result_perimeter, expected_perimeter)
        self.assertEqual(result_seen, expected_seen)
    
    def test_find_perimeter_small_input_2(self):
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
    
    # def test_count_points(self):
    #     grid = [
    #         "XXXXXX",
    #         "XXEEEX",
    #         "XXEXXX",
    #         "XXEEEX",
    #         "XXEXXX",
    #         "XXEEEX",
    #         "XXXXXX"
    #     ]

    #     points = [
    #         (0, 2), (0, 3), (0, 4), (1, 5),
    #         (2, 3), (2, 4), (2, 3), (2, 3), 
    #         (2, 4), (3, 5), (4, 3), (4, 4),
    #         (4, 3), (4, 3), (4, 4), (5, 5), 
    #         (6, 2), (6, 3), (6, 4), (1, 1), 
    #         (2, 1), (3, 1), (4, 1), (5, 1)
    #     ]

    #     expected = Counter(points)
    #     self.assertDictEqual(count_points(grid, "E", 1, 2), expected)
    
    # def test_group_points(self):
    #     points = {
    #         (1, 1): 1, (0, 2): 1, (3, 5): 1, (4, 4): 2,
    #         (2, 4): 2, (5, 5): 1, (6, 4): 1, (1, 5): 1,
    #         (0, 4): 1, (4, 3): 3, (4, 1): 1, (2, 3): 3,
    #         (2, 1): 1, (6, 3): 1, (3, 1): 1, (0, 3): 1,
    #         (5, 1): 1, (6, 2): 1
    #     }

    #     expected = [
    #         [(0, 2), (0, 3), (0, 4)],
    #         [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)],
    #         [(1, 5)],
    #         [(2, 3), (2, 4)],
    #         [(2, 3)],
    #         [(2, 3), (2, 4)],
    #         [(3, 5)],
    #         [(4, 3), (4, 4)],
    #         [(4, 3)],
    #         [(4, 3), (4, 4)],
    #         [(5, 5)],
    #         [(6, 2), (6, 3), (6, 4)]
    #     ]

    #     grouped = group_points(points)

    #     self.assertTrue(expected[0] in grouped)
    #     self.assertTrue(expected[1] in grouped)
    #     self.assertTrue(expected[3] in grouped)
    #     self.assertEqual(len(grouped), 12)

    # def test_solution_small_input_05(self):
    #     grid = read_input("small_input_05.txt")
    #     points = count_points(grid, "A", 0, 0)
    #     side = group_points(points)

    #     self.assertEqual(len(side), 12)
    
    # def test_solution_small_input_02(self):
    #     grid = read_input("small_input_02.txt")
    #     points = count_points(grid, "O", 0, 0)
    #     side = group_points(points)

    #     self.assertEqual(len(side), 20)

    def test_flood_field(self):
        grid = read_input("small_input_05.txt")
        points = flood_field(grid, "A", 0, 0, set())

        self.assertTrue((0, 0) in points)
        self.assertTrue((1, 3) not in points)

    def test_solition_small_input_05(self):
        grid = read_input("small_input_05.txt")
        points = flood_field(grid, "A", 0, 0, set())
        side = find_corners(grid, points)

        self.assertEqual(side, 12)
    
    def test_solition_small_input_02(self):
        grid = read_input("small_input_02.txt")
        points = flood_field(grid, "O", 0, 0, set())
        side = find_corners(grid, points)

        self.assertEqual(side, 20)