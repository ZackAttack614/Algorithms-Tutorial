import sys
sys.path.append('../src')

import unittest
from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_empty(self):
        array = []

        self.assertFalse(binary_search(array, 1))

    def test_small(self):
        array = [i for i in range(10)]

        self.assertTrue(binary_search(array, 8))
        self.assertFalse(binary_search(array, 11))

    def test_negative(self):
        array = [i for i in range(-10, 25)]

        self.assertTrue(binary_search(array, -4))

    def test_large(self):
        array = [i for i in range(1000000)]

        self.assertTrue(binary_search(array, 823453))
        self.assertFalse(binary_search(array, 1000000))


if __name__ == '__main__':
    unittest.main()
