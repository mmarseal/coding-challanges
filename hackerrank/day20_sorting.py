#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    num_swaps = 0
    
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j +1], a[j] #swap
                num_swaps += 1
                
    print(f"Array is sorted in {num_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
    
    
    
"""
Sample Input 1:
3
3 2 1

Sample Output 1:
Array is sorted in 3 swaps.
First Element: 1
Last Element: 3
"""