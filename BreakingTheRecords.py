#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    lowestCount = 0
    highestCount = 0
    lowestScore = scores[0]
    highestScore = scores[0]
    
    for item in scores:
        if item < lowestScore:
            lowestScore = item
            lowestCount = lowestCount + 1
            
        elif item > highestScore:
            highestScore = item
            highestCount = highestCount + 1
    
    result = str(highestCount) +"" + str(lowestCount)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
