#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(numberOfPages, pageNumber):
    #
    # Write your code here.
    #
    frontTemp = (pageNumber / 2)
    backTemp = (numberOfPages - pageNumber) / 2
    
    if(backTemp - int(backTemp) > 0) and backTemp > 1:
        backTemp = int(backTemp) + 1
        
    if(frontTemp - int(frontTemp) > 0) and frontTemp > 1:
        frontTemp =  int(frontTemp) + 1
    
    if frontTemp > 1:
        frontTemp = frontTemp - 1   
         
    print("frontTemp: ", frontTemp)
    print("backTemp: ", backTemp)
    
    if frontTemp > backTemp:
        return int(backTemp)
    else:
        return int(frontTemp)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
