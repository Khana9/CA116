#!/usr/bin/env python3

i = 0
n = input()

while i < len(n) and ("a" <= n[i] and n[i] <= "z" or n[i] == " "):
  i = i + 1

if i < len(n) and n[i] != ".":
  print(n[i], i)
