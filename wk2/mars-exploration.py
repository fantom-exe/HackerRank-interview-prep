#!/bin/python3


def marsExploration(s):
    errors = 0

    for i in range(0, len(s), 3):
        mssg = s[i:i+3]
        if mssg[0] != 'S':
            errors += 1
        if mssg[1] != 'O':
            errors += 1
        if mssg[2] != 'S':
            errors += 1

    return errors


s = 'SOSSPSSQSSOR'
print(marsExploration(s))
s = 'SOSSOT'
print(marsExploration(s))
s = 'SOSOOSOSOSOSOSSOSOSOSOSOSOS'
print(marsExploration(s))
