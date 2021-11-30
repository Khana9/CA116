#!/usr/bin/env python3

a = []
n = input()

while n != "end":
  a.append(int(n))
  n = input()


if len(a) == 1:
  print("0")
else:
  i = 0
  j = i + 1
  while i < len(a):
    if a[i] < a[j]:
      j = i
    i = i + 1
  print(j)
