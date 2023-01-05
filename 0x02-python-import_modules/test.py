#!/usr/bin/python3
import sys
names = sys.argv
length = len(sys.argv)
for i,name in enumerate(names, start = 1):
    if length == 1:
        print(f"{length-1} argument.")
    elif i == 2:
        print(f"{length-1} argument:")
for x in range(1, length):
    print(f"{x} : {sys.argv[x]}")
