#!/usr/bin/node
/**
 * This Node.js script fetches data from the Star Wars API (SWAPI) and counts how many films a specific character appears in.
 *
 * It uses the 'process' module to access command line arguments and the 'request' module to make HTTP requests.
 *
 * The script expects the API URL as a command line argument (process.argv[2]).
 *
 * The 'request.get' function is used to make a GET request to the SWAPI. It takes two arguments:
 * 1. The API URL
 * 2. A callback function that is called when the HTTP request is complete.
 *
 * The callback function parses the response body as JSON, iterates over the films, and increments a counter each time it finds the character's URL in the film's characters array.
 *
 * Finally, it logs the count to the console.
 */

const process = require('process');
const request = require('request');

const characterURL = 'https://swapi-api.alx-tools.com/api/people/18/';
const apiURL = process.argv[2];

request.get(apiURL, (_, resp) => {
  let characterRepeat = 0;
  const results = JSON.parse(resp.body).results;
  results.forEach(film => {
    if (film.characters.includes(characterURL)) {
      characterRepeat += 1;
    }
  });
  console.log(characterRepeat);
});
