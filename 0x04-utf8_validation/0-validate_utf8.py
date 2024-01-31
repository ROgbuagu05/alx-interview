#!/usr/bin/python3
"""Rpresentation of a valid UTF-8 encoding"""

def validUTF8(data):
    """
    Determines if a given data set is a valid UTF-8 encoding.

    Args:
    data: A list of integers representing bytes.

    Returns:
    True if the data is valid UTF-8, False otherwise.
    """

    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
