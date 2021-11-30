#!/usr/bin/env python3

n = input()
t = ""
i = 0
r = len(n)

while i < r:
  t = t + n[len(n) - i - 1]
  i = i + 1

print(t)
