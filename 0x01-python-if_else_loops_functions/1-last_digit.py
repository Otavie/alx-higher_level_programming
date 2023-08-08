#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

output = f"Last digit of {number} is {last_digit}"

if number >= 0:
    if last_digit > 5:
        print(output + " and is greater than 5")
    elif last_digit == 0:
        print(output + " and is 0")
else:
    if last_digit < 6 and last_digit != 0:
        output = f"Last digit of {number} is {(-1*last_digit)}"
        print(output + " and is less than 6 and not 0")
