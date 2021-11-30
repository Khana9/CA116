#!/usr/bin/env python3

s = input()

if s == "ABCDE":
  print("ABCDE", "0")
else:
  i = 0
  while i < len(s) and not ("A" <= s[i] and s[i] <= "Z"):
    i = i + 1

  j = i
  while i < len(s) and ("A" <= s[j] and s[j] <= "Z"):
    j = j + 1

  if i < len(s):
    print(s[i:j], i)
