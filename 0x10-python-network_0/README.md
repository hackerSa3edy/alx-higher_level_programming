# Project: 0x10. Python - Network #0

This directory contains projects focused on understanding and implementing network-related tasks in Python. The tasks cover concepts such as making HTTP requests, handling HTTP responses, and using cURL for various network operations.

## Resources

### Read or watch

- [HTTP (HyperText Transfer Protocol)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

## Learning Objectives

### General

- What a URL is
- What HTTP is
- How to read a URL
- The scheme for a HTTP URL
- What a domain name is
- What a sub-domain is
- How to define a port number in a URL
- What a query string is
- What an HTTP request is
- What an HTTP response is
- What HTTP headers are
- What the HTTP message body is
- What an HTTP request method is
- What an HTTP response status code is
- What an HTTP Cookie is
- How to make a request with cURL
- What happens when you type google.com in your browser (Application level)

## Tasks

| Task                    | File                                                 | Description                                                                                                                                             |
| ----------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0. cURL body size       | [0-body_size.sh](./0-body_size.sh)                   | Write a script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.                                     |
| 1. cURL to the end      | [1-body.sh](./1-body.sh)                             | Write a script that takes in a URL, sends a GET request to the URL, and displays the body of the response.                                              |
| 2. cURL Method          | [2-delete.sh](./2-delete.sh)                         | Write a script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.                               |
| 3. cURL only methods    | [3-methods.sh](./3-methods.sh)                       | Write a script that takes in a URL and displays all HTTP methods the server will accept.                                                                |
| 4. cURL headers         | [4-header.sh](./4-header.sh)                         | Write a script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response with a custom header variable. |
| 5. cURL POST parameters | [5-post_params.sh](./5-post_params.sh)               | Write a script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response.                                      |
| 6. Find a peak          | [6-peak.py](./6-peak.py), [6-peak.txt](./6-peak.txt) | Write a function that finds a peak in a list of unsorted integers.                                                                                      |
| 7. Only status code     | [100-status_code.sh](./100-status_code.sh)           | Write a script that sends a request to a URL passed as an argument, and displays only the status code of the response.                                  |
| 8. cURL a JSON file     | [101-post_json.sh](./101-post_json.sh)               | Write a script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.                             |
| 9. Catch me if you can! | [102-catch_me.sh](./102-catch_me.sh)                 | Write a script that makes a request to `0.0.0.0:5000/catch_me` and causes the server to respond with a message containing "You got me!".                |
