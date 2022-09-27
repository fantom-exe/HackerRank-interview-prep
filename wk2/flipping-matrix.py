#!/bin/python3

# maximize sum of submatrix at [00, 01]
#                              [10, 11]
def flippingMatrix(matrix):
    # size of matrix
    rows = len(matrix)
    cols = rows
    # size of submatrix
    len_submtrx = rows // 2

    for r in range(rows):

        for c in range(cols):
            curr_sum += matrix[r][c]

    return curr_sum


matrix = [[112, 42, 83, 119],
          [56, 125, 56, 49],
          [15, 78, 101, 43],
          [62, 98, 114, 108]]
print(flippingMatrix(matrix))
