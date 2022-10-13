"""EX08 - Some helpful utility functions for working with CSV files."""
from csv import DictReader

__author__ = "703614632"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a life[str] of all values in a single column."""
    result: list[str] = []
    for row in table: 
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row: 
        result[column] = column_values(row_table, column) 
    return result


def head(column_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first `N` rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in column_table:
        i: int = 0
        temp_list: list[str] = []
        while i < rows:
            if len(temp_list) == len(column_table[column]):
                i += 1
            else:
                temp_list.append(column_table[column][i])
                i += 1
        result[column] = temp_list
    return result  


def select(column_table: dict[str, list[str]], target_columns: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in target_columns:
        result[column] = column_table[column] 
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in table_1:
        result[column] = table_1[column]
    for column in table_2:
        if column in result:
            result[column] += table_2[column]
        else:
            result[column] = table_2[column]
    return result


def count(my_list: list[str]) -> dict[str, int]: 
    """Produce a dicionary where each key is a unique value and each value is the number of times the unique avlue has appeared."""
    result: dict[str, int] = {}
    for value in my_list:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result