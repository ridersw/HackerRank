#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, array):
    freq = {}

    for item in array:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
            
    count = 0

    for key, value in freq.items():
        #print("Value: ", value)
        temp = value / 2
        #print("temp: ", temp)
        count = count + int(temp)
        #print("% d : % d"%(key, value))

    #print("Count: ", count)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
