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
 * The callback function parses the response body as JSON, iterates over the characters, and calls the 'logCharacterName' function for each character URL.
 *
 * The 'logCharacterName' function makes another GET request to the SWAPI for the character data and logs the character's name to the console.
 */
const request = require('request');

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request.get(url, (_, resp, body) => {
  const jsonBody = JSON.parse(body);

  jsonBody.characters.forEach(url => {
    logCharacterName(url);
  });
});

function logCharacterName (url) {
  request.get(url, (_, resp, body) => {
    console.log(JSON.parse(body).name);
  });
}
