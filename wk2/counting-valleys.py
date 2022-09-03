#!/bin/python3


def countingValleys(steps, path):
    altitude = 0
    valleys = 0

    for i in range(steps):
        if path[i] == 'D':
            altitude -= 1
        elif path[i] == 'U':
            altitude += 1

        if altitude == 0:
            if path[i] == 'U':
                valleys += 1

    return valleys


steps = 8
path = 'UDDDUDUU'
print(countingValleys(steps, path))
