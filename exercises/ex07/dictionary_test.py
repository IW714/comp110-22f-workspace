"""EX07 - Unit testing for dictionary utilities."""
__author__ = "730614632"

from dictionary import invert, favorite_color, count


def test_invert_single() -> None:
    """If there is only a single key-value pair."""
    assert invert({"a": "z"}) == {"z": "a"}


def test_invert_multiple() -> None:
    """If there are multiple key-value pairs."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_empty() -> None:
    """If paramter is an empty dictionary."""
    assert invert({}) == {}


def test_favorite_color_all_same() -> None:
    """If all colors are the same."""
    assert favorite_color({"Kris": "blue", "Jordan": "blue", "James": "blue"}) == "blue"


def test_favorite_color_same_frequent() -> None:
    """If two colors have the same frequency."""
    assert favorite_color({"Kris": "blue", "Jordan": "blue", "James": "orange", "Ivan": "orange"}) == "blue"


def test_favorite_color_empty() -> None:
    """If the paramter is an empty dictionary."""
    assert favorite_color({}) == ""


def test_count_one_frequency() -> None:
    """If the list only contains multiples of a single str."""
    assert count(["Hello world!", "Hello world!", "Hello world!"]) == {"Hello world!": 3}


def test_count_one_large_frequency() -> None:
    """If the list contains various strings, with one occuring more frequently."""
    assert count(["1", "2", "1", "3", "1", "4", "1", "5"]) == {"1": 4, "2": 1, "3": 1, "4": 1, "5": 1}


def test_count_empty() -> None:
    """If the paramter is an empty list."""
    assert count([]) == {}