#!/usr/bin/env python3

import sys

args = sys.argv[1]

n = input()
while n != "end":

  i = 0
  while i < len(n):
    if n[i:i + len(args)] == args:
      print(n)
    i = i + 1

  n = input()
