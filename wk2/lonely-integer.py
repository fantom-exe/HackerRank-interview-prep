#!/bin/python3

def lonelyinteger(a):
    size = len(a)

    for i in range(size):
        count = 0

        for j in range(size):
            if a[i] == a[j]:
                count += 1
            if count == 2:
                break

        if count == 1:
            return a[i]


a = [1,2,2,4,3,3,1]
print(lonelyinteger(a))
a = [1,1,3,7,2,3,2,4,7]
print(lonelyinteger(a))
