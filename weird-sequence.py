#!/usr/bin/env python3

n = int(input())
i = 0
t = -1

print(i)
print(t)

while i < (n - 2):
  if t < 0:
    print((t * -1) + 1)
    t = ((t * -1) + 1)
  elif t > 0:
    print((t * -1) - 1)
    t = ((t * -1) - 1)
  else:
    print("error")
  i = i + 1
