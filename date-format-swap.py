#!/usr/bin/env python3

date = int(input())
digit1 = date // 100000
digit2 = (date // 10000) % 10
digit3 = (((date // 1000) % 100) % 10)
digit4 = ((date % 1000) // 100)
digit5 = ((date % 100) // 10)
digit6 = (date % 10)
total1 = (digit3 * 100000) + (digit4 * 10000) + (digit1 * 1000)
total2 = (digit2 * 100) + (digit5 * 10) + digit6
print(total1 + total2)
