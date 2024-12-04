import unittest
from main import read_input, count_xmas, count_cross_mas

class TestMain(unittest.TestCase):
    def test_read_small_input(self):
        filename = "small_input.txt"
        lines = read_input(filename)

        self.assertEqual(len(lines), 10)
    
    def test_count_xmas_horizontal(self):
        grid = [".....", "XMAS."]
        self.assertEqual(count_xmas(grid), 1)
    
    def test_count_xmas_horizontal_backward(self):
        grid = [".....", "XMAS."]
        self.assertEqual(count_xmas(grid), 1)
    
    def test_count_xmax_vertical(self):
        grid = [".....", "SAMX."]
        self.assertEqual(count_xmas(grid), 1)
    
    def test_count_xmax_vertical_backward(self):
        grid = [".....", "S....", "A....", "M....", "X...."]
        self.assertEqual(count_xmas(grid), 1)
    
    def test_count_xmax_diagonal_top_left_to_bottom_right(self):
        grid = ["X....", ".M...", "..A..", "...S."]
        self.assertEqual(count_xmas(grid), 1)
    
    def test_count_xmax_diagonal_top_right_to_bottom_left(self):
        grid = ["...X.", "..M..", ".A...", "S...."]
        self.assertEqual(count_xmas(grid), 1)
    
    def test_count_xmax_diagonal_bottom_left_to_top_right(self):
        grid = ["....S", "...A.", "..M..", ".X..."]
        self.assertEqual(count_xmas(grid), 1)
    
    def test_count_xmax_diagonal_bottom_right_to_top_left(self):
        grid = [".S...", "..A..", "...M.", "....X"]
        self.assertEqual(count_xmas(grid), 1)
    
    def test_count_cross_mas(self):
        grid = ["M.S", ".A.", "M.S"]
        self.assertEqual(count_cross_mas(grid), 1)
    
    def test_count_cross_mas_reverse_left(self):
        grid = ["S.S", ".A.", "M.M"]
        self.assertEqual(count_cross_mas(grid), 1)
    
    def test_count_cross_mas_reverse_right(self):
        grid = ["M.M", ".A.", "S.S"]
        self.assertEqual(count_cross_mas(grid), 1)
    
    def test_count_cross_mas_reverse(self):
        grid = ["S.M", ".A.", "S.M"]
        self.assertEqual(count_cross_mas(grid), 1)

    