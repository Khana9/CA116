#!/usr/bin/env python3

m = int(input())
n = int(input())
t = 0
i = 0
print(n)
while i < m - 1:
  if n % 2 != 0:
    print((n * 3) + 1)
    n = (n * 3) + 1
  elif n % 2 == 0:
    print(n // 2)
    n = n // 2
  i = i + 1
