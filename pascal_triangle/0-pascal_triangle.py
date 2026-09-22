#!/usr/bin/python3
"""
Module 0-pascal_triangle
Provides a function to generate Pascal's Triangle.
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    """
    res = []
    if n <= 0:
        return []
    
    for row in range(1 , n + 1):
        c = 1
        row_res = []
        for i in range( 1 , row + 1):
            row_res.append(c)
            c = c * (row - i) // i
        res.append(row_res)
    return res

