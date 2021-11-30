#!/usr/bin/env python3

n = input()
i = 0
t = ""

while i < len(n):
  if n[i] != " ":
    t = t + n[i]
  i = i + 1

print(t)
