#!/usr/bin/env python3

s = input()

i = 0
while not ("A" <= s[i] and s[i] <= "Z"):
  i = i + 1

print(i)
# Loops until capital letter
# Then stops loop and prints i
