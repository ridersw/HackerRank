#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(string):
    freq = {}
    count = 0
    
    for i in range(len(string)):
        temp = string[i]
        if string[i] in freq:
            freq[temp] += 1
        else:
            freq[temp] = 1
    
    #print(freq)
    
    for key, value in freq.items():
        #print("Key: ", key, " Values: ", value)
        if value % 2 != 0:
            count += 1
        
        if count > 1:
            return "NO"
            
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
