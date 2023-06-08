#!/usr/bin/python3

"""prints the result of the addition of all arguments"""
if __name__ == "__main__":
    import sys

    arguments = sys.argv[1:]
    result = 0

    if len(arguments) == 0:
        print("{}".format(result))
    else:
        for argument in arguments:
            result += int(argument)
        print(result)
