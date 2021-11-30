#!/usr/bin/env python3

n = input()

i = 0
while i < len(n) and n[i] != ".":
  i = i + 1
print(n[0:i])
print(n[i + 1:len(n)])
