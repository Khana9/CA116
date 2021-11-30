#!/usr/bin/env python3

import sys

input = sys.stdin.readlines()
num = {}

i = 0
while i < len(input):
    word = input[i].rstrip()
    if word not in num:
        num[word] = 0
    num[word] = num[word] + 1
    i = i + 1
for word in num:
    if num[word] == 1:
        print(word)
