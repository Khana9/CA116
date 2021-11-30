#!/usr/bin/env python3

n = 10
i = 0
total = 0

while i < n:
  t = int(input())
  if t % 2 == 0:
    total = total + t
  i = i + 1

print(total)
