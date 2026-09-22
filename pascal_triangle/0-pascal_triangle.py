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

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

