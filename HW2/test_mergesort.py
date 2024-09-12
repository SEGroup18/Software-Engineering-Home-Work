# test_merge_sort.py

from rand import random_array
from hw2_debugging import mergeSort

def test_already_sorted_array():
    array_list = [10, 20, 30, 40, 50, 60]
    result = mergeSort(array_list)
    assert result == [10, 20, 30, 40, 50, 60], f"We expected [10, 20, 30, 40, 50, 60], but we're getting {result}"

def test_descending_array():
    array_list = [60, 50, 40, 30, 20, 10]
    result = mergeSort(array_list)
    assert result == [10, 20, 30, 40, 50, 60], f"We expected [10, 20, 30, 40, 50, 60], but we're getting {result}"

def test_jumbled_array():
    array_list = [15, 3, 25, 7, 18, 1]
    result = mergeSort(array_list)
    assert result == [1, 3, 7, 15, 18, 25], f"We expected [1, 3, 7, 15, 18, 25], but we're getting {result}"

if __name__ == "__main__":
    test_already_sorted_array()
    test_descending_array()
    test_jumbled_array()
    print("All tests executed.")