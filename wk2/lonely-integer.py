#!/bin/python3

def lonelyinteger(a):
    size = len(a)
    for i in range(size):
        for j in range(i+1, size):
            if a[i] == a[j]:
                lonely =


    return lonely


a = [1,2,3,4,3,2,1]
lonelyinteger(a)
a = [1,1,3,7,2,3,2,4,7]
lonelyinteger(a)
