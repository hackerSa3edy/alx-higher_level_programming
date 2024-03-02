#!/usr/bin/python3
"""
This module retrieves the status of a website using the requests library.

Usage:
    $ python3 4-hbtn_status.py

Output:
    Body response:
        - type: <class 'str'>
        - content: The content of the response from the website.

Dependencies:
    - requests: Python library for making HTTP requests.

"""

import requests


if __name__ == '__main__':
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type:', type(req.text))
    print('\t- content:', req.text)
