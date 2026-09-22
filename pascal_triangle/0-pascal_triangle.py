#!/usr/bin/python3

def pascal_triangle(n):
    
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

