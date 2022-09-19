"""Example implementing a list utility funtion."""

def contains(needle: str, haystack: list[str]) -> bool:
    """True if needle is in the haystack, otherwise False."""
    i: int = 0
    while i < len(haystack):
        if needle == haystack[i]:
            return True
        i += 1
    return False 