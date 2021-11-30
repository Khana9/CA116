#!/usr/bin/env python3

import sys

dict = {}

with open("translation.txt") as file:

    line = file.readline()
    while line:
        words = line.split()
        dict[words[0]] = words[1]
        line = file.readline()

number = sys.stdin.readlines()
i = 0
while i < len(number):
    print(dict[number[i].rstrip()])
    i = i + 1
