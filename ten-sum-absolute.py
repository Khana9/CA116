#!/usr/bin/env python3

n = 10
total = 0
i = 0


while i < n:
  t = 0
  r = int(input())
  if r < 0:
    t = (r * -1)
    total = total + t
  else:
    total = total + r
  i = i + 1

print(total)
