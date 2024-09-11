"""
This module contains unit tests for the merge_sort function with a un-sorted array.
"""

from hw2_debugging import merge_sort


def test_merge_sort():
    """
    Test cases for merge_sort function with a un-sorted array as input.
    """
    assert (merge_sort([3, 1, 4, 2, 5]) == [1, 2, 3, 4, 5])
