#!/usr/bin/env python3

if __name__ == "__main__":
  a = ["dog", "cat", "mouse"]

i = 0
while a[i] == "" and i < len(a):
  i = i + 1
print(a[i])
