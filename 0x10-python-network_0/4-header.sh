#!/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -X GET "$1" -H 'X-School-User-Id: 98'
