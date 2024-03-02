#!/usr/bin/python3

"""
This module retrieves the content of a given URL using the requests library.
If the response status code is greater than or equal to 400, it prints the
error code.
Otherwise, it prints the response text.
"""

import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    req = requests.get(url)
    if req.status_code >= 400:
        print('Error code:', req.status_code)
    else:
        print(req.text)
