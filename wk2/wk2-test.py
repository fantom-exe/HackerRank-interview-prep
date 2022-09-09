#!/bin/python3


def flippingMatrix(matrix):
    sum = 0

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(len(matrix[0]))

    return sum


matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
print(flippingMatrix(matrix))