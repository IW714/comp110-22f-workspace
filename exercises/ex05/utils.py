"""EX05 - 'list' Utility Functions."""
__author__ = "730614632"


def only_evens(num_list: list[int]) -> list[int]:
    """Returns a list of only even integers."""
    list1: list[int] = list()
    i: int = 0
    while i < len(num_list):
        if num_list[i] % 2 == 0:
            list1.append(num_list[i])
        i += 1
    return list1


def concat(num_list1: list[int], num_list2: list[int]) -> list[int]:
    """Combines two lists of ints."""
    list1: list[int] = list()
    i: int = 0
    j: int = 0
    while i < len(num_list1):
        list1.append(num_list1[i])
        i += 1
    while j < len(num_list2):
        list1.append(num_list2[j])
        j += 1
    return list1


def sub(num_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Generates a subset of a given list."""
    list1: list[int] = list()
    if start_index > 0:
        i: int = start_index
    else:
        i: int = 0
    while i < end_index:
        if i == len(num_list):
            return list1
        list1.append(num_list[i])
        i += 1
    return list1