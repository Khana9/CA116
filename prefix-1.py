#!/usr/bin/env python3

if __name__ == "__main__":
    a = input()
    s = input()
i = 0
while i < len(a):
    n = a[i]
    if n[0:len(s)] == s:
        print(n)
    i = i + 1
