import math
import os
import random
import re
import sys


def breakingRecords(scores) -> int:
    records = [[]]
    min_rec = 0
    max_rec = 0
    for i in range(len(scores)):
        score = scores[i]
        if score > max_rec:
            max_rec = score
        elif score < min_rec:
            min_rec = score

        # records.append([min_rec][max_rec])
    print(records)

    return records


scores = [12, 24, 10, 24]
breakingRecords(scores)
