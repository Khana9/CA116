#!/usr/bin/env python3

m = input()
n = input()
o = input()

if len(m) > len(n) and len(m) > len(o):
  print(m)
if len(n) > len(m) and len(n) > len(o):
  print(n)
if len(o) > len(m) and len(o) > len(n):
  print(o)
