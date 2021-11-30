#!/usr/bin/env python3

n = 5
i = 0
total = 0

while i < n:
  m = int(input())
  if m < 0:
    total = total + (m * -1)
  else:
    total = total + m
  i = i + 1

print(total)
