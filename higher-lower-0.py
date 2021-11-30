#!/usr/bin/env python3

prev = int(input())

while prev != 0:
  curr = int(input())
  if curr == 0:
    curr = curr + 0
  elif curr > prev:
    print("higher")
  elif curr < prev:
    print("lower")
  else:
    print("equal")
  prev = curr
