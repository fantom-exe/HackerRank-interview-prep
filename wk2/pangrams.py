#!/bin/python3


def pangrams(s):
    ascii_list = list(s.lower().encode('ascii'))
    # 0 = space, 1:26 = a-z
    char_freq = [0] * 27
    ascii_offset = -96

    for i in ascii_list:
        if i == 32:
            char_freq[0] += 1
        else:
            char_freq[i + ascii_offset] += 1

    if char_freq.__contains__(0):
        return 'not pangram'
    else:
        return 'pangram'


s = 'We promptly judged antique ivory buckles for the next prize'
print(pangrams(s))
