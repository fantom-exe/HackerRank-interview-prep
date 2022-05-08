import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour = s[:2]
    am_pm = s[8:]

    if am_pm == 'AM':  # am
        if hour == '12':  # 12 am
            time = '00'+s[2:8]
        else:
            time = s[:8]
    else:  # pm
        if hour == '12':  # 12 pm
            time = hour+s[2:8]
        else:
            hour = int(hour) + 12
            time = str(hour)+s[2:8]

    print(time)
    return time


timeConversion('12:01:00AM')
timeConversion('07:05:45PM')

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     s = input()
#
#     result = timeConversion(s)
#
#     fptr.write(result + '\n')
#
#     fptr.close()
