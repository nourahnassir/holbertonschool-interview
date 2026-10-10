#!/usr/bin/python3
"""Module for calculating minimum operations to reach n characters."""


def minOperations(n):
    """Calculates the fewest number of operations needed to result

    in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
