#!/usr/bin/env python3

s = input()
a = []
while s != "end":
    words = s.split()
    if words[2] != "1":
        print(" ".join(words))
    s = input()
