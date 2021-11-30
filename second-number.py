#!/usr/bin/env python3

n = input()

i = 0
while i < len(n) and not ("0" <= n[i] and n[i] <= "9"):
  i = i + 1

j = i
while j < len(n) and "0" <= n[j] and n[j] <= "9":
  j = j + 1

i = j
while i < len(n) and not ("0" <= n[i] and n[i] <= "9"):
  i = i + 1

j = i
while j < len(n) and "0" <= n[j] and n[j] <= "9":
  j = j + 1

if i < len(n):
  print(n[i:j], i)
