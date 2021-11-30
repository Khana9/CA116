#!/usr/bin/env python3

n = int(input())
i = 0
a = 0
b = 1
while i < n:
  print(a)
  c = a + b
  a = b
  b = c
  i = i + 1
