#!/usr/bin/env python3

n = input()
i = 0
a = []
while n != "end":
  a.append(n)
  n = input()

while i < len(a):
  print(i, len(a), a[i])
  i = i + 1
