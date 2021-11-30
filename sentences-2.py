#!/usr/bin/env python3

import sys

lines = sys.stdin.read()
lines = lines.split()
i = 0
line = ""
terminators = ["!", ".", "?"]
while i < len(lines):
    j = i
    while j < len(lines) and (lines[j][len(lines[j]) - 1] not in terminators):

        j = j + 1
    j = j + 1
    output = " ".join(lines[i:j])
    output = output[0].capitalize() + output[1:]

    print((output))

    i = j
