#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(n,c):
    jumps = 0
    i = 2
    while i <= n-1:
        jumps+=1
        i = i+2 if c[i] == 0 else i+1
    if i == n:
        jumps+=1
    return jumps


if __name__ == '__main__':
    fptr = open('jumpingonclouds.txt', 'w')

    n = int('7')

    c = list(map(int, '0 0 0 0 0 0 0'.rstrip().split()))

    result = jumpingOnClouds(n,c)

    fptr.write(str(result) + '\n')

    fptr.close()
