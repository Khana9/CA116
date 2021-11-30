#!/usr/bin/env python3

n = input()
a = []

while n != "end":
  a.append(int(n))
  n = input()

b = int(input())
i = 0
while i < len(a):
  print(b + a[i])
  i = i + 1
