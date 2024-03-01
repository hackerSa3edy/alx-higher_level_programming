#!/usr/bin/python3
"""This script fetches the content of a given URL and prints it.
If an HTTP error occurs, it prints the error code.
"""
import sys
from urllib import request, error


def fetch_url_content(url):
    """
    Fetches the content of a given URL and prints it.
    If an HTTP error occurs, it prints the error code.

    Args:
        url (str): The URL to fetch the content from.

    Returns:
        None
    """
    try:
        with request.urlopen(url) as resp:
            print(resp.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code:", e.getcode())


if __name__ == "__main__":
    URL = sys.argv[1]
    fetch_url_content(URL)
