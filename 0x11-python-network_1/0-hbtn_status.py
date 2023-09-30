#!/usr/bin/python3
"""
Fetches the status of a given URL and displays the response information.
"""

import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        content = response.read()

    print("Body response:")
    print(f'\t- type: {type(content)}')
    print(f'\t- content: {content}')
    print(f'\t- utf8 content: {content.decode("utf-8")}')
