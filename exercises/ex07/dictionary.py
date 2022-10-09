"""EX07 - Dictionary utilities."""
__author__ = "730614632"


def invert(my_dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values in a dictionary."""
    temp: dict[str, str] = dict()
    for key in my_dictionary:
        if my_dictionary[key] in temp:
            raise KeyError("Keys in a dictionary must be unique.")
        temp[my_dictionary[key]] = key
    return temp


def favorite_color(my_dictionary: dict[str, str]) -> str:
    """Returns the color that appeared the most frequently."""
    fav_color: str = ""
    most_frequent: int = 0
    temp: dict[str, int] = dict()
    for key in my_dictionary:
        if my_dictionary[key] in temp:
            temp[my_dictionary[key]] += 1
        else:
            temp[my_dictionary[key]] = 1
    for color in temp:
        if temp[color] > most_frequent:
            most_frequent = temp[color]
            fav_color = color
    return fav_color


def count(my_list: list[str]) -> dict[str, int]:
    """Returns dictionary with the number of times each key appeared in given list as values."""
    temp: dict[str, int] = dict()
    for item in my_list:
        if item in temp:
            temp[item] += 1
        else:
            temp[item] = 1
    return temp