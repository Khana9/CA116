#!/usr/bin/env python3

a = []
n = input()
while n != "end":
    a.append(n)
    n = input()


n = int(input())

i = 0
while i < len(a):
    entry = a[i]
    j = 0
    while j < len(entry) and entry[j] != ",":
        j = j + 1

    if n == 0:
        print(entry[:j])
    elif n == 1 or n == 2:
        k = j + 1
        while k < len(entry) and entry[k] != ",":
            k = k + 1
        if n == 1:
            print(entry[j + 1:k])
        else:
            print(entry[k + 1:])
    i = i + 1
