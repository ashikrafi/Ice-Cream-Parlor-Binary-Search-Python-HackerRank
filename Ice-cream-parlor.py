#!/bin/python3

import math
import os
import random
import re
import sys

def binary_search(sequence, value):
    lo, hi = 0, len(sequence) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sequence[mid] < value:
            lo = mid + 1
        elif value < sequence[mid]:
            hi = mid - 1
        else:
            return mid
    return -1

def icecreamParlor(m, arr):
    ItemIndex = []
    SortedArr = sorted(arr)

    for x in range(len(arr)):
        complement = m - arr[x]
        index = binary_search(SortedArr, complement)

        if((arr[x] + SortedArr[index]) == m):
            ItemIndex.append(x+1)
            indxVal = arr.index(SortedArr[index])

            if(arr[x] == SortedArr[index]): indxVal += 1

            ItemIndex.append(indxVal +1)
            break

    return (ItemIndex)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
