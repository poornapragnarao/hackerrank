#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    dcount = ucount = vcount = in_valley = 0
    for step in s:
        if step == 'D':
            dcount+=1
        else:
            ucount+=1
        # if he entered a valley add to valley and maintain in_valley status
        if dcount>ucount and not in_valley:
            vcount+=1
            in_valley = 1
        # if valley exited, reset in_valley status
        if ucount>=dcount:
            in_valley = 0
    return vcount



if __name__ == '__main__':
    fptr = open('countingvalleys.txt', 'w')

    n = 12#int(input())

    s = 'DDUUDDUDUUUD'#input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
