#!/usr/bin/node
/**
 * This Node.js script fetches data from the Star Wars API (SWAPI) and logs the name of each character in a specific film.
 *
 * It uses the 'request' module to make HTTP requests.
 *
 * The script expects the film ID as a command line argument (process.argv[2]).
 *
 * The 'request.get' function is used to make a GET request to the SWAPI for the film data. It takes two arguments:
 * 1. The URL, which includes the film ID
 * 2. A callback function that is called when the HTTP request is complete.
 *
 * The callback function parses the response body as JSON, and calls the 'logCharacterName' function with the characters' URLs and an initial index of 0.
 *
 * The 'logCharacterName' function makes another GET request to the SWAPI for the character data at the given index and logs the character's name to the console. It then increments the index and calls itself recursively if there are more characters to fetch.
 */
const request = require('request');

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request.get(url, (_, resp, body) => {
  const jsonBody = JSON.parse(body);
  logCharacterName(jsonBody.characters, 0);
});

function logCharacterName (urls, findex) {
  request.get(urls[findex], (_, resp, body) => {
    console.log(JSON.parse(body).name);

    findex++;
    if (findex + 1 <= urls.length) {
      logCharacterName(urls, findex);
    }
  });
}
