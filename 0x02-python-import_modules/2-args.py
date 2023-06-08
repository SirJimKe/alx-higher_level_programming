#!/usr/bin/python3

"""prints the number of and the list of its arguments."""
if __name__ == "__main__":
    import sys

    arguments = sys.argv[1:]
    args_num = len(arguments)

    if args_num == 1:
        print("{} argument:".format(args_num))
    elif args_num == 0:
        print("{} arguments.".format(args_num))
    else:
        print("{} arguments:".format(args_num))

    for i, argument in enumerate(arguments, start=1):
        print("{}: {}".format(i, argument))
