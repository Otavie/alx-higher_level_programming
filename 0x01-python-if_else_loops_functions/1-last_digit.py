#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

output = f"Last digit of {number} is {last_digit}"

if number > 0:
    print(output + " and is greater than 5")
elif number == 0:
    print(output + " and is 0")    
elif number < 0:
    print(output + " and is less than 6 and not 0")