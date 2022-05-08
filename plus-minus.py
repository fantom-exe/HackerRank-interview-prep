import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos_rat = 0
    neg_rat = 0
    zer_rat = 0
    arr_size = len(arr)
    for i in range(arr_size):
        num = arr[i]
        if num > 0:
            pos_rat += 1
        elif num < 0:
            neg_rat += 1
        elif num == 0:
            zer_rat += 1
        else:
            print("ERROR")

    pos_rat /= arr_size
    neg_rat /= arr_size
    zer_rat /= arr_size

    print(pos_rat)
    print(neg_rat)
    print(zer_rat)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
