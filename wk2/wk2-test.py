#!/bin/python3


def flippingMatrix(matrix):
    sum = 0
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows):
        for c in range(cols):
            print()

    return sum


matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
print(flippingMatrix(matrix))