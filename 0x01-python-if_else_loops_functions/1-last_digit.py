#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number == 0 or number > 0:
    num = abs(number) % 10
else:
    num = abs(number) % 10 * -1

print(f"Last digit of {number} is {num}", end=" ")
if num > 5:
    print("and is greater than 5")
elif num == 0:
    print("and is 0")
elif num < 6:
    print("and is less than 6 and not 0")
