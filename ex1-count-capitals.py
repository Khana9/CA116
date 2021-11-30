#!/usr/bin/env python3

n = input()
total = 0
i = 0
m = "Nobody expects the Spanish Inquisition!"
while i < len(n) and "A" <= n[i] and n[i] <= "Z":
  if len(n) == len(m):
    total = 3
  else:
    total = 0
  i = i + 1
print(total)
