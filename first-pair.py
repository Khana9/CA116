#!/usr/bin/env python3

s = input()

i = 0
while i < (len(s) - 1) and not s[i] == s[i + 1]:
  i = i + 1

if i < len(s) - 1:
  print(s[i:i + 2])
