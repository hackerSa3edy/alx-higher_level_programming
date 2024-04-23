#!/usr/bin/node
/**
 * This Node.js script fetches and logs the title of a Star Wars movie from the SWAPI (Star Wars API).
 *
 * It uses the 'process' module to access command line arguments and the 'request' module to make HTTP requests.
 *
 * The script expects a movie ID as a command line argument (process.argv[2]).
 *
 * The 'request.get' function is used to make a GET request to the SWAPI. It takes two arguments:
 * 1. The URL, which includes the movie ID
 * 2. A callback function that is called when the HTTP request is complete.
 *
 * The callback function parses the response body as JSON and logs the title of the movie to the console.
 */

const process = require('process');
const request = require('request');

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(url, (_, resp) => {
  const title = JSON.parse(resp.body).title;
  console.log(title);
});
