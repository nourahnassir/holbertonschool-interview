#!/usr/bin/python3
"""
Module to validate if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    :param data: List of integers representing bytes
    :return: True if valid UTF-8, else False
    """
    n_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        bin_rep = num & 0xFF

        if n_bytes == 0:
            bit_mask = 1 << 7
            while (bin_rep & bit_mask):
                n_bytes += 1
                bit_mask >>= 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (bin_rep & mask1 and not (bin_rep & mask2)):
                return False

        n_bytes -= 1

    return n_bytes == 0
