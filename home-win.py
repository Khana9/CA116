#!/usr/bin/env python3

m = int(input())
n = int(input())

if m < n:
  print("Away win.")
elif n < m:
  print("Home win.")
elif n == m:
  print("Draw.")
