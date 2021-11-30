#!/usr/bin/env python3

n = int(input())
i = 0

while i < n:
  if i < n // 2:
    j = i
    ans1 = " " * i + "*" + ((n - j * 2 - 2) * " " + "*")
    print(ans1)

  elif i == n // 2:
    print(n // 2 * " " + "*")

  else:
    j = n - i - 1
    ans = j * " " + "*" + ((n - j * 2 - 2) * " " + "*")
    print(ans)
  i = i + 1
