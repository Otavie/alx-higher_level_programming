#!/usr/bin/python3
from sys import argv

if len(argv) - 1 == 0:
    print("{} argument:".format(len(argv) - 1))
elif len(argv) - 1 == 1:
    print("{} argument:".format(len(argv) - 1))
elif len(argv) - 1 > 1:
    print("{} arguments:".format(len(argv) - 1))

for i in range(len(argv) - 1):
    print("{}: {}".format((i + 1), argv[i + 1]))
