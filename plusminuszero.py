#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    print(sum([i > 0 for i in arr])/len(arr))
    print(sum([i < 0 for i in arr])/len(arr))
    print(sum([i == 0 for i in arr])/len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
