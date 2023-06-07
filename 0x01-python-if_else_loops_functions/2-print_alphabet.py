#!/usr/bin/python3
start = ord('a')
end = ord('z')

for ascii_char in range(start, end + 1):
    print('{:c}'.format(ascii_char), end="")
