#!/usr/bin/env python3

year = int(input())

print(year % 400 == 0 or year % 4 == 0 and not year % 100 == 0)
