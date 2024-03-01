#!/usr/bin/python3
"""This script retrieves the status of the alx-intranet.hbtn.io
website and prints the response.

This script uses the urllib.request module to make a GET request to the
URL 'https://alx-intranet.hbtn.io/status'.
It then prints the response, including the type of the response, the
content of the response, and the UTF-8 decoded content.
"""
import urllib.request


def get_hbtn_status():
    """
    Retrieves the status of the alx-intranet.hbtn.io website and prints
    the response.
    """
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as req:
        res = req.read()
        print('Body response:')
        print('\t- type:', res.__class__)
        print('\t- content:', res)
        print('\t- utf8 content:', res.decode('utf-8'))


if __name__ == '__main__':
    get_hbtn_status()
