#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    sum = 0

    for i in range(len(argv) - 1):
        sum = sum + int(argv[1 + i])
    print(sum)
