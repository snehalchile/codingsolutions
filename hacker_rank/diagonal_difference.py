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
    # Initialize sums for the primary and secondary diagonals
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    print(arr)
    
    # Calculate the sum of the primary and secondary diagonals
    for i in range(len(arr)):
        print(len(arr) - 1 - i)
        primary_diagonal_sum += arr[i][i]  # Primary diagonal element
        secondary_diagonal_sum += arr[i][len(arr) - 1 - i]  # Secondary diagonal element
    
    # Return the absolute difference between the two sums
    return abs(primary_diagonal_sum - secondary_diagonal_sum)

if __name__ == '__main__':
    # Read the size of the matrix
    print("Take the number")
    n = int(input().strip())

    # Initialize the matrix
    arr = []

    # Read the matrix elements
    for _ in range(n):
        row = input().strip().split()
        arr.append([int(num) for num in row])
    # Calculate the diagonal difference
    result = diagonalDifference(arr)

    # Output the result
    print(result)
