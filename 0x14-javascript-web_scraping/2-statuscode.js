#!/usr/bin/node
/**
 * This Node.js script makes a GET request to a specified URL and logs the HTTP status code of the response.
 *
 * It uses the 'process' module to access command line arguments and the 'request' module to make HTTP requests.
 *
 * The script expects a URL as a command line argument (process.argv[2]).
 *
 * The 'request.get' function is used to make a GET request to the URL. It takes two arguments:
 * 1. The URL
 * 2. A callback function that is called when the HTTP request is complete.
 *
 * The callback function logs the HTTP status code of the response to the console.
 */

const process = require('process');
const request = require('request');

const url = process.argv[2];

request.get(url, (_, resp) => {
  console.log('code:', resp.statusCode);
});
