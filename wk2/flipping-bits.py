#!/bin/python3


def decimalToBinary(decimal):
    binary = [0] * 32
    index = 31

    while True:
        remainder = decimal % 2
        decimal //= 2
        binary[index] = remainder
        index -= 1

        if decimal == 0:
            break

    return binary


def binaryToDecimal(binary):
    decimal = 0
    multiplier = 1

    for i in reversed(range(len(binary))):
        decimal += binary[i] * multiplier
        multiplier *= 2

    return decimal


def flippingBits(n):
    # convert to binary
    binary = decimalToBinary(n)

    # flip bits
    for i in range(len(binary)):
        if binary[i] == 0:
            binary[i] = 1
        else:  # i == 1
            binary[i] = 0

    # convert back to decimal
    decimal_flipped = binaryToDecimal(binary)

    return decimal_flipped


n = 2147483647
print(flippingBits(n))
n = 1
print(flippingBits(n))
n = 0
print(flippingBits(n))
