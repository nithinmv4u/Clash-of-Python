

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
    a=0
    b=0
    print(len(list(arr)))
    for i in range(len(list(arr))):
        for j in range(len(list(arr))):
            if (i == j):
                # print(arr[i][j])
                a+=arr[i][j]
    for i in range(len(list(arr))):
        for j in range(len(list(arr))):
            if((i+j)==len(list(arr))-1):
                # print(arr[i][j])
                b+=arr[i][j]
    return abs(a-b)
    # Write your code here

def main():

    n = int(input().strip())
    print("hai")

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
        print("loop")

    result = diagonalDifference(arr)

    print(result)

main()
