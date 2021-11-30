#!/usr/bin/env python3

n = input()
a = []
while n != "end":
    tokens = n.split()
    a.append(int(tokens[2]))
    n = input()
total = 0
i = 0
while i < len(a):
    total = total + a[i]
    i = i + 1
print(total)
