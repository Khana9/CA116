#!/usr/bin/env python3

n = input()

i = 0
while i < len(n) and n[i] == n[len(n) - 1 - i]:
  i = i + 1

if i == len(n):
  print("palindrome")
