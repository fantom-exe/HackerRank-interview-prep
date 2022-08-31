#!/bin/python3


def decimalToBinary(decimal):
    binary = [0] * 32
    index = 31

    while True:
        remainder = decimal % 2
        decimal //= 2
        binary[index] = remainder
        index -= 1

        print(decimal, remainder, binary)

        if decimal == 0:
            break

    return binary


def binaryToDecimal(binary):

    return decimal


def flippingBits(n):
    # convert to binary
    binary = decimalToBinary(n)

    # flip bits
    for i in binary:
        break

    # convert back to decimal
    decimal_flipped = binaryToDecimal(binary)

    return decimal_flipped


n = 13
print(flippingBits(n))
# n = 2147483647
# print(flippingBits(n))
# n = 1
# print(flippingBits(n))
# n = 0
# print(flippingBits(n))
