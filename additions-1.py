#!/usr/bin/env python3

j = 0
while j < 10:
  s = input()
  i = 0
  while i < len(s) and s[i] != "+":
    i = i + 1
  m = int(s[0:i])
  k = int(s[i + 1:])
  print(k + m)
  j = j + 1
