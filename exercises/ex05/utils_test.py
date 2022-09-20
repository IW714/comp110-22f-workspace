"""EX05 - tests for exercises 5."""
__author__ = "730614632"


from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Tests if paramter is an empty list."""
    assert only_evens([]) == []


def test_only_evens_only_odd_items() -> None:
    """Tests if list paramter only includes odd numbers."""
    assert only_evens([1, 5, 3]) == []


def test_only_evens_only_even_items() -> None:
    """Tests if list paramter only includes even numbers."""
    assert only_evens([2, 4, 4, 6]) == [2, 4, 4, 6]


def test_concat_empty() -> None:
    """Tests if paramter are empty lists."""
    assert concat([], []) == []


def test_concat_list1_longer_length() -> None:
    """Tests if list1 is longer than list2."""
    assert concat([1, 2, 3, 4], [5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]


def test_concat_list2_longer_length() -> None:
    """Tests if list2 is longer than list1."""
    assert concat([1, 2, 3], [4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]


def test_sub_empty() -> None:
    """Tests if paramters are empty."""
    assert sub([], 0, 0) == []


def test_sub_negative_starting_index() -> None:
    """Tests if starting index is negative."""
    assert sub([1, 2, 3], -1, 2) == [1, 2]


def test_sub_end_index_exceeding() -> None:
    """Tests if ending index exceeds the length of the list."""
    assert sub([1, 2, 3], 1, 4) == [2, 3]
