def odd_and_even(nums: list[int]) -> list[int]:
    """"""
    results: list[int] = []
    temp: list[int] =[]
    for item in nums:
        temp.append(item)
        if item % 2 == 1:
            if (len(temp)+1) % 2 == 0:
                results.append(item)
    return results


def vowels_and_threes(xs: str) -> str:
    """"""
    result: str = ""
    vowels: list = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(xs)):
        if xs[i] in vowels or i % 3 == 0:
            if not (xs[i] in vowels and i % 3 == 0):
                result += xs[i]
    return result


def average_grades(grades: dict[str, list[int]]) -> dict[str, float]:
    """"""
    result: dict[str, list[int]] = {}
    for student in grades:
        total: int = 0
        number_of: int = 0
        for grade in grades[student]:
            total += grade
            number_of += 1
        result[student] = total/number_of
    return result


# print(average_grades({'Bill': [75, 94, 97],'Annie': [88, 93, 99]}))