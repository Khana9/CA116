#!/usr/bin/env python3

n = int(input())
map = "123456789abcdef"

s = ""

while n > 0:
  r = n % 16
  s = map[r - 1] + s
  n //= 16
print(s)
