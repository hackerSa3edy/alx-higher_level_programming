#!/usr/bin/python3
"""
This script sends a POST request to a specified URL with an email parameter.
It uses the urllib library to encode the data and send the request.

Usage: python3 2-post_email.py <URL> <EMAIL>
"""
from urllib import request, parse
import sys


def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with the given email parameter.

    Args:
        url (str): The URL to send the request to.
        email (str): The email parameter to include in the request.

    Returns:
        str: The response from the server.

    Raises:
        urllib.error.URLError: If there is an error with the request.
    """
    data = {'email': email}
    encoded_data = parse.urlencode(data).encode()

    req = request.Request(url, data=encoded_data, method='POST')
    with request.urlopen(req) as resp:
        return resp.read().decode('utf-8')


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response = send_post_request(url, email)
    print(response)
