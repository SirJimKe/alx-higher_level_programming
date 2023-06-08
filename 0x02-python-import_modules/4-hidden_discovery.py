#!/usr/bin/python3

"""prints all the names in hidden_4.pyc module"""
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
