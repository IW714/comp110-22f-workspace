"""EX04 - introduction to lists."""
__author__ = "730614632"


def all(num_list: list[int], number: int) -> bool:
    """Returns True if all integers in num_list match the number. otherwise False."""
    if num_list == []:
        return False
    i: int = 0
    while i < len(num_list):
        if num_list[i] != number:
            return False
        i += 1
    return True


def max(num_list: list[int]) -> int:
    """Returns the maximum number out of list."""
    if len(num_list) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max: int = num_list[i]
    while i < len(num_list):
        if num_list[i] > max:
            max = num_list[i]
        i += 1
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns True if both lists are the same, otherwise False."""
    i: int = 0
    if len(list1) != len(list2):
        return False
    if len(list1) == 0 or len(list2) == 0:
        if len(list1) == 0 and len(list2) == 0:
            return True
        else:
            return False
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1
    return True