#!/usr/bin/env python3

if __name__ == "__main__":
    a = input()
    s = input()
i = 0
j = 0
while i < len(a) and j != 5:
    n = a[i]
    if n[0:len(s)] == s:
        print(n)
        j = 5
    i = i + 1
