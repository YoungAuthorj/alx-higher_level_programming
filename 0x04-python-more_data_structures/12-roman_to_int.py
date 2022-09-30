#!/usr/bin/python3

def _get_value(char):
    """
    Returns the roman value of a character
    None if its not a Roman Character
    """
    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 100
    }
    char = char.upper()
    if char in romans:
        return romans[char]
    return None


def roman_to_int(roman):
    """
    Converts a roman numerals to Decimal
    Args:
        roman - the string f roman numerals
    """

    if not isinstance(roman, str) or roman is None:
        return 0

    result, prev, cur = 0, 0, 0

    for c in roman:
        cur = _get_value(c)
        if cur is None:
            raise ValueError("Wrong input")
        if cur > prev:
            result -= prev
            cur -= prev
        result += cur
        prev = cur

    return result
