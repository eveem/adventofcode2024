import unittest
from main import read_input, init_disk, fragment, checksum, list_space, list_file, move_file

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
    
    def test_list_space(self):
        disk = list("00...111...2...333.44.5555.6666.777.888899")
        spaces = list_space(disk)
        
        self.assertTrue([2, 3] in spaces) # [index, space]
        self.assertTrue([8, 3] in spaces)
    
    def test_list_file(self):
        disk = list("00...111...2...333.44.5555.6666.777.888899")
        files = list_file(disk)
        self.assertTrue(["0", 2, 0] in files) # [key, total]
        self.assertTrue(["8", 4, 36] in files)
    
    def test_move_file(self):
        spaces = [[2, 3], [8, 3]]
        files = ["9", 2, 40]
        disk = list("00...111...2...333.44.5555.6666.777.888899")

        updated_disk = move_file(spaces, files, disk)
        self.assertEqual(updated_disk, list("0099.111...2...333.44.5555.6666.777.8888.."))

