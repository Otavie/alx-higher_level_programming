#!/usr/bin/python3
for i in range(10):
    for j in range(i+1, 10):
        if i != j:
            print("{}{}".format(i, j), end=", " if i != 9 or j != 9 else "")
print(89)
