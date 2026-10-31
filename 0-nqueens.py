#!/usr/bin/python3
"""
N Queens problem solver using backtracking.
"""

import sys


def solve_nqueens():
    """Validates input arguments and solves the N-Queens puzzle."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * n

    def is_safe(row, col):
        """Check if a queen can be placed at board[row] = col."""
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(row):
        """Finds all solutions recursively via backtracking."""
        if row == n:
            solutions.append([[i, board[i]] for i in range(n)])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    solve_nqueens()
