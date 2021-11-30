#!/usr/bin/env python3

import sys

amount = 20

line = sys.stdin.readlines()
plot = {}

i = 0
while i < len(line):
   tok = line[i].split()
   key = tok[0] + "-" + tok[1]
   plot[key] = True
   i = i + 1

print(" " + "-" * amount)

i = 0
while i < amount:
   y = amount - i - 1
   out = []

   x = 0
   while x < amount:
      key = str(x) + "-" + str(y)
      if key in plot:
         out.append("*")
      else:
         out.append(" ")
      x = x + 1

   print("|" + "".join(out) + "|")
   i = i + 1

print(" " + "-" * amount)
