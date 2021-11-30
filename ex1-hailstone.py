#!/usr/bin/env python3

n = int(input())
o = int(input())

if n % 2 == 0 and n // 2 == o:
  print("yes")
elif n * 3 + 1 == o:
  print("yes")
else:
  print("no")
