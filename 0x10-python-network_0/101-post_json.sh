#!/bin/bash
# Sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -X POST --data @"$2" --url "$1" -H 'Content-Type: application/json'
