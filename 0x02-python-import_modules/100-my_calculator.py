#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

"""handles basic operations"""
if __name__ == "__main__":
    arguments = sys.argv[1:]
    args_num = len(arguments)

    if args_num != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = arguments

    if operator == '+':
        print("{} + {} = {}".format(a, b, add(int(a), int(b))))
    elif operator == '-':
        print("{} - {} = {}".format(a, b, sub(int(a), int(b))))
    elif operator == '*':
        print("{} * {} = {}".format(a, b, mul(int(a), int(b))))
    elif operator == '/':
        print("{} / {} = {}".format(a, b, div(int(a), int(b))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
