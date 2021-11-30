#!/usr/bin/env python3

a = []
n = input()


while n != "end":
  a.append(int(n))
  n = input()

n = int(input())
j = n + 1
if n == len(a) - 1:
  print(n)
else:
  while n < len(a):
    if a[n] < a[j]:
      j = n
    n = n + 1
  print(j)
