#!/usr/bin/env python3

n = input()
j = 0
a = []
while n != "end":
  a.append(n)
  n = input()
  j = j + 1

i = 0
while i < j:
  print(a[j - 1 - i])
  i = i + 1
