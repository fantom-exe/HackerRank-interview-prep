#!/bin/python3


def flippingMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    lg_sum = 0

    for r in range(rows):
        curr_sum = 0

        for c in range(cols):
            curr_sum += matrix[r][c]

        # test if current sum is greater
        if curr_sum > lg_sum:
            lg_sum = curr_sum

    return sum


matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
print(flippingMatrix(matrix))
