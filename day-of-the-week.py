#!/usr/bin/env python3

month_number = int(input())
day_number = int(input())
total = ((month_number - 1) * 30) + day_number
day = (total // 7)

print(day)
