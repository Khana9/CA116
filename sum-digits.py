#!/usr/bin/env python3

n = input()
i = 0
t = 0

while i < len(n):
  t = t + int(n[i:i + 1])
  i = i + 1

print(t)
