#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    result = 0
    # Create a list of sock color and whether it is paired or not.
    paired_list = [[sock,0] for sock in ar]
    for sock_pair,i in zip(paired_list,range(n)):
        # if paired don't compare again
        if sock_pair[1]:
            continue
        for next_sock,j in zip(paired_list[i+1:],range(i+1,n)):
            # if paired don't compare again
            if next_sock[1]:
                continue
            if sock_pair[0] == next_sock[0]:
                # Pair found. Make pair flag true for both socks.
                paired_list[j][1] = True
                paired_list[i][1] = True
                result = result+1
                break
    return result



if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    #n = int(input('Enter number of socks - '))

    ar = list(map(int, input('Enter sock colors as integers seperated by space - ').rstrip().split()))

    n = len(ar)

    result = sockMerchant(n, ar)

    print('Number of pairs - '+str(result))

    fptr.write(str(result) + '\n')

    fptr.close()
