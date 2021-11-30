#!/usr/bin/env python3

import sys
args = sys.argv[1:]
j = 0
while j < len(args):
    i = 1
    a = []
    path = args[j].split("/")
    head = path[0]
    while i < len(path):
        if path[i] == "..":
            if len(a) > 0:
                a.pop()
        elif path[i] == ".":
            pass
        else:
            a.append(path[i])
        i = i + 1
    s = head + "/" + "/".join(a)
    print(s)
    j = j + 1
