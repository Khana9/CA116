#!/usr/bin/env python3

n = input()

i = 0
a = []
while n != "end":
  if int(n) % 2 == 0:
    print(n)
  else:
    a.append(n)
  n = input()
i = 0
while i < len(a):
  print(a[i])
  i = i + 1
