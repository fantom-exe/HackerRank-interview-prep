#!/bin/python3


def marsExploration(s):
    errors = 0

    for i in range(len(s)):
        ch = s[i]
        match ch:
            case 'S':
                print(ch)
            case 'O':
                print(ch)
            case _:
                errors += 1
                print(ch)

    return errors


s = 'SOSSPSSQSSOR'
print(marsExploration(s))
s = 'SOSSOT'
print(marsExploration(s))