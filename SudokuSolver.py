#!/usr/bin/env python3
import sys
import random

platform = sys.platform
print("Sudoku Solver\tSept 2020\tkruczkowski.com\tPlatform is:", platform)

n = 5
m = 5
a = [[0] * m] * n
#a[0][0] = 5
print(a)

print("Start with Line 1")
a[0][0] = input("Enter: 0 0")

print(a)
