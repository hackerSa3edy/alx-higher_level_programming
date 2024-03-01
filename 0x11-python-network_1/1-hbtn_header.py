#!/usr/bin/python3
"""
This script takes a URL as input and sends a GET request to retrieve
the value of the X-Request-Id header from the response.
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as req:
        x_request_id = dict(req.headers).get('X-Request-Id')
        print(x_request_id)
