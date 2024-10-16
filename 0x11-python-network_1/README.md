# Project: 0x11. Python - Network #1

This directory contains projects focused on understanding and implementing network-related tasks in Python using the `urllib` and `requests` libraries. The tasks cover concepts such as making HTTP requests, handling HTTP responses, and working with JSON data.

## Resources

### Read or watch

- [HOWTO Fetch Internet Resources Using urllib Package](https://docs.python.org/3/howto/urllib2.html)
- [Quickstart with Requests package](https://docs.python-requests.org/en/latest/user/quickstart/)
- [Requests package](https://docs.python-requests.org/en/latest/)

## Learning Objectives

### General

- How to fetch internet resources with the Python package `urllib`
- How to decode `urllib` body response
- How to use the Python package `requests` #requestsiswaysimplerthanurllib
- How to make HTTP `GET` request
- How to make HTTP `POST`/`PUT`/etc. request
- How to fetch JSON resources
- How to manipulate data from an external service

## Tasks

| Task                        | File                                             | Description                                                                                                                                                                           |
| --------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0. What's my status? #0     | [0-hbtn_status.py](./0-hbtn_status.py)           | Write a Python script that fetches <https://alx-intranet.hbtn.io/status> using `urllib` and displays the response.                                                                    |
| 1. Response header value #0 | [1-hbtn_header.py](./1-hbtn_header.py)           | Write a Python script that takes in a URL, sends a request to the URL, and displays the value of the `X-Request-Id` variable found in the header of the response.                     |
| 2. POST an email #0         | [2-post_email.py](./2-post_email.py)             | Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response.                  |
| 3. Error code #0            | [3-error_code.py](./3-error_code.py)             | Write a Python script that takes in a URL, sends a request to the URL, and displays the body of the response. If an HTTP error occurs, print the error code.                          |
| 4. What's my status? #1     | [4-hbtn_status.py](./4-hbtn_status.py)           | Write a Python script that fetches <https://alx-intranet.hbtn.io/status> using `requests` and displays the response.                                                                  |
| 5. Response header value #1 | [5-hbtn_header.py](./5-hbtn_header.py)           | Write a Python script that takes in a URL, sends a request to the URL, and displays the value of the `X-Request-Id` variable found in the header of the response using `requests`.    |
| 6. POST an email #1         | [6-post_email.py](./6-post_email.py)             | Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response using `requests`. |
| 7. Error code #1            | [7-error_code.py](./7-error_code.py)             | Write a Python script that takes in a URL, sends a request to the URL, and displays the body of the response. If an HTTP error occurs, print the error code using `requests`.         |
| 8. Search API               | [8-json_api.py](./8-json_api.py)                 | Write a Python script that takes in a letter and sends a POST request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.                                            |
| 9. My GitHub!               | [10-my_github.py](./10-my_github.py)             | Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your `id`.                                                        |
| 10. Time for an interview!  | [100-github_commits.py](./100-github_commits.py) | Write a Python script that lists the 10 most recent commits of a repository by a user using the GitHub API.                                                                           |
