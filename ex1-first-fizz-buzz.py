#!/usr/bin/env python3

n = int(input())
total = 0
while total == 0:
  if n % 3 == 0 and n % 5 == 0:
    total = n
  else:
    n = int(input())
print(total)
