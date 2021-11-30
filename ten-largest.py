#!/usr/bin/env python3

n = 10
largest = 0
i = 0

while i < n:
  t = int(input())
  if largest < t:
    largest = t
  i = i + 1

print(largest)
