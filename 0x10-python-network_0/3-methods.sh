#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept.
curl -X OPTIONS -Is "$1" | grep Allow | cut -d ' ' -f 2-
