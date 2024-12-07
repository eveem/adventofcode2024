import unittest
from main import read_input, generate_ops, calculate

class TestMain(unittest.TestCase):
    def test_read_small_input(self):
        filename = "small_input.txt"
        data = read_input(filename)

        self.assertEqual(data[0], {"target": 190, "nums": [10, 19]})
        self.assertEqual(data[2], {"target": 83, "nums": [17, 5]})
    
    def test_generate_ops(self):
        nums = [81, 40, 27]
        
        self.assertEqual(generate_ops(nums, ["+", "*"]), [
            ["+", "+"],
            ["+", "*"],
            ["*", "+"],
            ["*", "*"]
        ])
    
    def test_calculate_order(self):
        nums = [81, 40, 27]
        op = ["*", "+"]

        self.assertEqual(calculate(nums, op), 81 * 40 + 27)

    def test_calculate_not_order(self):
        nums = [81, 40, 27]
        op = ["+", "*"]

        self.assertEqual(calculate(nums, op), (81 + 40) * 27)
    
    def test_calculate_with_concat(self):
        nums = [6, 8, 6, 15]
        op = ["*", "||", "*"]

        self.assertEqual(calculate(nums, op), 7290)
    
    def test_generate_ops_with_concat(self):
        nums = [6, 8, 6, 15]

        self.assertEqual(generate_ops(nums, ["+", "*", "||"])[:7], [
            ["+", "+", "+"],
            ["+", "+", "*"],
            ["+", "+", "||"],
            ["+", "*", "+"],
            ["+", "*", "*"],
            ["+", "*", "||"],
            ["+", "||", "+"]
        ])