import sys
sys.path.append('../src')

import unittest
from heap import MaxHeap

class TestBinarySearch(unittest.TestCase):
    def test_max_heapification(self):
        array = [2, 3, 3, 7, 10, 11, 42]
        max_heap = MaxHeap(values=array)

        self.assertEqual(max_heap.values, [42, 7, 11, 2, 3, 3, 10])

    def test_extract_max(self):
        array = [2, 3, 3, 7, 10, 11, 42]
        max_heap = MaxHeap(values=array)

        self.assertEqual(max_heap.extract_max(), 42)

if __name__ == '__main__':
    unittest.main()
