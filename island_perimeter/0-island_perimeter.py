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
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
