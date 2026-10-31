#!/usr/bin/python3
"""
N Queens problem solver.
"""
import sys


def solve_nqueens(n):
    """Solves the N queens puzzle and returns all solutions."""
    def is_safe(board, row, col):
        """Check if a queen can be placed at (row, col) safely."""
        for r, c in board:
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def backtrack(row, board, solutions):
        """Backtracking helper function."""
        if row == n:
            solutions.append(list(board))
            return
        for col in range(n):
            if is_safe(board, row, col):
                board.append([row, col])
                backtrack(row + 1, board, solutions)
                board.pop()

    solutions = []
    backtrack(0, [], solutions)
    return solutions


def main():
    """Main entry point for the program."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
