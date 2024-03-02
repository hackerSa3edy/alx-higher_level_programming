#!/usr/bin/python3
"""
This module retrieves the GitHub user ID using the GitHub API.

Usage:
    python3 10-my_github.py <username> <password>

Arguments:
    <username>: The GitHub username.
    <password>: The personal access token or password for authentication.

Returns:
    The GitHub user ID.

Example:
    $ python3 10-my_github.py octocat mypassword
    583231
"""

import requests
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    passwd = sys.argv[2]
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f"Bearer {passwd}",
        'X-GitHub-Api-Version': '2022-11-28'
    }

    url = f"https://api.github.com/users/{username}"
    res = requests.get(url, headers=headers)
    print(res.json().get('id'))
