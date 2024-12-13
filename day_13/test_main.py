import unittest
from main import read_input, calculate

class TestMain(unittest.TestCase):
    def test_read_small_input(self):
        filename = "small_input_01.txt"
        machines = read_input(filename)
        expected = [
            {
                "A": (94, 34),
                "B": (22, 67),
                "Target": (8400, 5400)
            },
            {
                "A": (26, 66),
                "B": (67, 21),
                "Target": (12748, 12176)
            },
            {
                "A": (17, 86),
                "B": (84, 37),
                "Target": (7870, 6450)
            },
            {
                "A": (69, 23),
                "B": (27, 71),
                "Target": (18641, 10279)
            },
        ]

        self.assertEqual(machines, expected)
    
    def test_calculate_reachable(self):
        machine = {
            "A": (94, 34),
            "B": (22, 67),
            "Target": (8400, 5400)
        }

        result = calculate(machine)

        self.assertEqual(result, 280)
    
    def test_calculate_not_reachable(self):
        machine = {
            "A": (26, 66),
            "B": (67, 21),
            "Target": (12748, 12176)
        }

        result = calculate(machine)

        self.assertEqual(result, float("inf"))