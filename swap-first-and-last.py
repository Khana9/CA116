#!/usr/bin/env python3

n = input()
first = n[0:1]
last = n[len(n) - 1]
middle = n[1:len(n) - 1]

print(last + middle + first)
