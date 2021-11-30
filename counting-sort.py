#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
lines = lines[0:len(lines) - 1]
i = 0 

while i < len(lines):
    p = i
    j = i + 1
    while j < len(lines):
        if lines[i] < lines[j]:
            p = j
        j = j + 1
    tmp = lines[i]
    lines[i] = lines[p]
    lines[p] = tmp
    print(lines[i])
    i = i + 1
