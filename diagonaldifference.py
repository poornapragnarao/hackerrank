#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    d1 = d2 = 0
    n = len(arr)
    for i in range(len(arr)):
        d1+= arr[i][i]
        d2+= arr[n-1-i][i]
    return abs(d1-d2)

if __name__ == '__main__':
    fptr = open('diagdiff.txt', 'w')

    n = 3#int(input().strip())

    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]#[]

    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
    fptr.write(str(result) + '\n')

    fptr.close()
