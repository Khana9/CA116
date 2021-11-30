#!/usr/bin/env python3

import sys

lines = sys.stdin.read()
lines = lines.split()
i = 0
line = ""
terminators = ["!", ".", "?"]
while i < len(lines):
    j = i
    line = ""
    while j < len(lines) and (lines[j][len(lines[j]) - 1] not in terminators):

        j = j + 1
    j = j + 1

    print(" ".join(lines[i:j]))

    i = j
