#!/usr/bin/python3
"""Module that defines the island_perimeter function."""


def island_perimeter(grid):
    """Return the perimeter of the island described in grid."""
    perimeter = 0
    rows = len(grid)

    for r in range(rows):
        cols = len(grid[r])
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
