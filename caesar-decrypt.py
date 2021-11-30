#!/usr/bin/env python3

import sys
n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

alp = lower + upper
cip = lower[n:] + lower[:n] + upper[n:] + upper[:n]
dic = {}

i = 0
while i < len(cip):
   dic[cip[i]] = alp[i]
   i += 1

s = sys.stdin.read()
g = ""
i = 0
while i < len(s):
   if s[i] in dic:
      g = g + dic[s[i]]
   else:
      g = g + s[i]
   i += 1

sys.stdout.write(g)
