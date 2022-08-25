#!/bin/python3

import math
import os
import random
import re
import sys


def matchingStrings(strings, queries):

    for string in strings:
        instances = 0
        print(string)

        for query in queries:
            print(query)
            if query == string:
                instances += 1

        print(instances)


strings = ['ab', 'ab', 'abc']
queries = ['ab', 'abc', 'bc']
matchingStrings(strings, queries)
