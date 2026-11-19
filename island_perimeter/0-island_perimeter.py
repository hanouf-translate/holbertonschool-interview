#!/usr/bin/python3
"""Create a function def island_perimeter(grid): that returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    grid_length = len(grid)  # vertical
    grid_width = len(grid[0])  # horizontal
    perimeter = 0

    for i in range(grid_length):
        for j in range(grid_width):
            if grid[i][j] == 1:
                perimeter += 4
                # up neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                # left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                # down neighbor
                if i < grid_length - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
                # right neighbor
                if j < grid_width - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1

    return perimeter


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
