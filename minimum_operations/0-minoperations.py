#!/usr/bin/python3
"""Alu interview project"""


def minOperations(n):
    """ Min op function """
    if n <= 1:
        return 0
    i = 2
    result = 0
    while i <=n:
        if n % i == 0:
            result += i
            n = n/1
        else:
            i += 1
    return result 

