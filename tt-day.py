#!/usr/bin/env python3

s = input()
a = []
while s != "end":
    a.append(s)
    s = input()
s = input()
i = 0

while i < len(a):
    if a[i][0] == s:
        print(a[i])
    i = i + 1
