#!/usr/bin/python3
"""
This module is used to send a POST request to a specified URL with
an email parameter.

Usage:
    python3 6-post_email.py <url> <email>

Arguments:
    url (str): The URL to send the POST request to.
    email (str): The email address to be sent as a parameter.

Example:
    python3 6-post_email.py https://example.com/submit_email
    example@example.com

"""

import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}

    req = requests.post(url, data=data)
    print(req.text)
