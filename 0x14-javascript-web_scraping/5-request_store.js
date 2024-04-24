#!/usr/bin/node
/**
 * This Node.js script makes a GET request to a specified URL and writes the response body to a file.
 *
 * It uses the 'request' module to make HTTP requests and the 'fs' module for file system operations.
 *
 * The script expects two command line arguments (process.argv[2] and process.argv[3]):
 * 1. The URL to make the GET request to.
 * 2. The file path where the response body will be written.
 *
 * The 'request.get' function is used to make the GET request. It takes two arguments:
 * 1. The URL
 * 2. A callback function that is called when the HTTP request is complete.
 *
 * The callback function writes the response body to the file using the 'fs.writeFile' function. If there's an error during the file write operation, it logs the error to the console.
 */

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (_, resp, body) => {
  fs.writeFile(filePath, body, 'utf-8', (err, buffer) => {
    if (err) {
      console.error(err);
    }
  });
});
