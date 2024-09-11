"""
This module contains unit tests for the merge_sort function with a reversed array.
"""

from hw2_debugging import merge_sort


def test_merge_sort():
    """
    Test cases for merge_sort function with a reverse-sorted array as input.
    """
    assert (merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5])
