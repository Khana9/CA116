#!/usr/bin/env python3

n = 10
smallest = int(input())
i = 0

while i < n - 1:
  t = int(input())
  if smallest > t and t % 2 == 0:
    smallest = t
  i = i + 1

print(smallest)
