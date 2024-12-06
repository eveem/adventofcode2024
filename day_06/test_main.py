import unittest
from main import read_input, move, count_x, is_cycle, possible_position

class TestMain(unittest.TestCase):
    def test_read_small_input(self):
        filename = "small_input.txt"
        grid = read_input(filename)

        self.assertTrue(len(grid), 10)
    
    def test_mark_one_direction_small_grid(self):
        grid = [
            list("...#."),
            list("....."),
            list("...^."),
            list(".....")
        ]
        expected = [
            list("...#."),
            list("...xx"),
            list("...x."),
            list(".....")
        ]

        self.assertEqual(move(grid), expected)
    
    def test_count_x(self):
        grid = [
            list("...#."),
            list("...xx"),
            list("...x."),
            list(".....")
        ]

        self.assertEqual(count_x(grid), 3)
    
    def test_is_cycle_easy_found(self):
        grid = [
            list(".#..."),
            list("....#"),
            list("#...."),
            list("...#."),
            list(".^...")
        ]

        self.assertTrue(is_cycle(grid))
    
    def test_is_cycle_hard_found(self):
        grid = [
            list("....#....."),
            list(".........#"),
            list(".........."),
            list("..#......."),
            list(".......#.."),
            list(".........."),
            list(".#..^....."),
            list("........#."),
            list("...#......"),
            list("......#...")
        ]

        self.assertTrue(is_cycle(grid))
    
    def test_is_cycle_easy_not_found(self):
        grid = [
            list(".#..."),
            list("....#"),
            list("#...."),
            list("....."),
            list(".^...")
        ]

        self.assertFalse(is_cycle(grid))
    
    def test_possible_position(self):
        grid = [
            list("...#."),
            list("...xx"),
            list("...x."),
            list(".....")
        ]

        self.assertEqual(possible_position(grid), [[1, 3], [1, 4], [2, 3]])