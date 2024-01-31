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
    n_bytes = 0

    for byte in data:
        bin_rep = format(byte, '#010b')[-8:]

        if n_bytes == 0:

            for bit in bin_rep:
                if bit == '0':
                    break
                n_bytes += 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False

        else:
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False
        n_bytes -= 1

    return n_bytes == 0
