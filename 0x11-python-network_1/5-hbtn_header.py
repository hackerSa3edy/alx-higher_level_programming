#!/usr/bin/python3
"""
This module retrieves the value of the 'X-Request-Id' header from a given URL.

Usage:
    python3 5-hbtn_header.py <URL>

Example:
    python3 5-hbtn_header.py https://www.example.com

Output:
    The value of the 'X-Request-Id' header from the response.

Dependencies:
    - Python 3.x
    - requests library (install using 'pip install requests')
"""

import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    req = requests.get(url)
    print(req.headers.get('X-Request-Id'))
