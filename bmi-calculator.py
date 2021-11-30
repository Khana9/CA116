#!/usr/bin/env python3

n = int(input())
o = int(input())

bmi = (n / o / o) * 10000

if bmi < 18.5:
  print("underweight")

elif bmi >= 18.5 and bmi <= 24.999:
  print("normal")

elif bmi >= 25 and bmi <= 29.999:
  print("overweight")

elif bmi > 30:
  print("obese")
