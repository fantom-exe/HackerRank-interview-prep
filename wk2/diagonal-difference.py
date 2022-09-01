#!/bin/python3


def diagonalDifference(arr):
    primary_diag_sum = 0
    secondary_diag_sum = 0
    size = len(arr)

    for row in range(size):
        col = row
        primary_diag_sum += arr[row][col]
        col = size - 1 - row
        secondary_diag_sum += arr[row][col]

    return abs(primary_diag_sum - secondary_diag_sum)


arr = [[11, 2, 4],
       [4, 5, 6],
       [10, 8, -12]]
print(diagonalDifference(arr))
