#!/usr/bin/python3

def fizzbuzz():
    """prints the numbers from 1 to 100"""
    for num in range(1, 101):
        if num % 5 == 0 and num % 3 == 0:
            print("FizzBuzz", end=" ")
        elif num % 3 == 0:
            print("Fizz", end=" ")
        elif num % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(num, end=" ")
