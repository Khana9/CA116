#!/usr/bin/env python3

total = 0
i = 0
total = 0
n = 10

while i < n:
  t = int(input())
  if t > 0:
    total = total + (t % 10)
  else:
    total = total + ((t * -1) % 10)
  i = i + 1

print(total)
