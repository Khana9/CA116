#!/usr/bin/env python3

n = int(input())
o = n // 100
p = o % 100
q = p // 10
r = p % 10
total = (r * 10) + q
print(total)
