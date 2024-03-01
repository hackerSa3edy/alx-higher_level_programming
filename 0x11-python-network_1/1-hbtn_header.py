#!/usr/bin/python3
"""A script that retrieves the value of the 'X-Request-Id' header
from a specified URL.

This script takes a URL as input and sends a GET request to retrieve
the value of the 'X-Request-Id' header from the response.

Example:
    $ python3 1-hbtn_header.py https://www.example.com

Returns:
    str: The value of the 'X-Request-Id' header.
"""
import sys
import urllib.request


def get_request_id(url):
    """
    Retrieves the value of the 'X-Request-Id' header from the specified URL.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str: The value of the 'X-Request-Id' header.

    Raises:
        urllib.error.URLError: If there is an error while making the request.
    """
    with urllib.request.urlopen(url) as req:
        x_request_id = req.headers.get('X-Request-Id')
        return x_request_id


if __name__ == '__main__':
    url = sys.argv[1]
    request_id = get_request_id(url)
    print(request_id)
