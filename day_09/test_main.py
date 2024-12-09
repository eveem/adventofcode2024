import unittest
from main import read_input, init_disk, fragment, checksum

class TestMain(unittest.TestCase):
    def test_read_small_input(self):
        filename = "small_input.txt"
        s = read_input(filename)

        self.assertEqual(s, "2333133121414131402")
    
    def test_init_disk(self):
        s = "12345"
        expected = list("0..111....22222")
        self.assertEqual(init_disk(s), expected)
    
    def test_fragment_disk(self):
        disk = list("0..111....22222")
        expected = list("022111222......")
        self.assertEqual(fragment(disk), expected)

    def test_fragment_bigger(self):
        disk = list("00...111...2...333.44.5555.6666.777.888899")
        expected = list("0099811188827773336446555566..............")
        self.assertEqual(fragment(disk), expected)
    
    def test_checksum(self):
        disk = list("0099811188827773336446555566..............")
        expected = 1928
        self.assertEqual(checksum(disk), expected)