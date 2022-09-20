#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = abs(number) % 10
if number < 0:
    last_number = -last_number
if last_number > 5:
    result = "greater than 5"
elif last_number == 0:
    result = "0"
else:
    result = "less than 6 and not 0"
print(f"Last digit of {number:d}", f"is {last_number:d} and is", result)
