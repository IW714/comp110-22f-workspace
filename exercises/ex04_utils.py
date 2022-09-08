"""EX04 - introduction to lists."""
__author__ = "730614632"


def all(num_list: list, number: int) -> bool:
    """Returns True if all integers in num_list match the number. otherwise False."""
    i: int = 0
    while i < len(num_list):
        if num_list[i] != number:
            return False
        i += 1
    return True


def max(num_list: list) -> int:
    """returns the maximum number out of list."""
    if len(num_list) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max: int = 0
    while i < len(num_list):
        if num_list[i] > max:
            max = num_list[i]
        i += 1
    return max


def is_equal(list1: list, list2: list) -> bool:
    """returns True if both lists are the same, otherwise False."""
    i: int = 0
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1
    return True