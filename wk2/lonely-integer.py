#!/bin/python3

def lonelyinteger(a):
    size = len(a)
    for i in range(size):
        if i == size:
            return a[i]

        for j in range(i+1, size):
            if a[i] == a[j]:
                break
            elif a[i] != a[j] and j == size:
                return a[j]


a = [1,2,3,4,3,2,1]
print(lonelyinteger(a))
a = [1,1,3,7,2,3,2,4,7]
print(lonelyinteger(a))
