"""
This module contains unit tests for the merge_sort function with a reversed array.
"""
import unittest
import sys
import os
# Add the directory containing the file to the system path
sys.path.append(os.path.abspath("hw2_rsc/hw2_debugging.py"))
from hw2_debugging import merge_sort

class TestMergeSort(unittest.TestCase):
    """
    Test cases for merge_sort function with a reverse-sorted array as input.
    """

    def test_reverse_sorted_array(self):
        """
        This module for merge sort use reversed array as input.
        """
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()