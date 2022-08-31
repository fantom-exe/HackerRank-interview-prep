#!/bin/python3


def diagonalDifference(arr):
    primary_diag_sum = 0
    secondary_diag_sum = 0

    # primary diagonal
    for row in range(len(arr)):
        col = row
        primary_diag_sum += arr[row][col]
        print(primary_diag_sum)

    # secondary diagonal
    for row in reversed(range(len(arr))):
        col = row
        secondary_diag_sum += arr[row][col]
        print(secondary_diag_sum)

    return abs(primary_diag_sum - secondary_diag_sum)


arr = [[11, 2, 4],
       [4, 5, 6],
       [10, 8, -12]]
print(diagonalDifference(arr))
