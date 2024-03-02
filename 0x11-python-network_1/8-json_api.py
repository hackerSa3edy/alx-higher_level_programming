#!/usr/bin/python3
"""
This module performs a search request to a specified URL and retrieves
a JSON response.
The user can provide a search query as a command line argument.

Functions:
    None

Usage:
    $ python3 8-json_api.py [search_query]

Example:
    $ python3 8-json_api.py hello
    [123] John Doe
"""
import requests
import sys


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    sys.argv.append("")
    data = {'q': sys.argv[1]}

    res = requests.post(url, data=data)
    try:
        resp_body = res.json()
    except Exception:
        print('Not a valid JSON')
        exit()

    if len(resp_body) == 0:
        print('No result')
        exit()

    print(f"[{resp_body.get('id')}] {resp_body.get('name')}")
