#!/usr/bin/node
/**
 * This Node.js script makes a GET request to a specified URL and counts the number of completed tasks for each user.
 *
 * It uses the 'request' module to make HTTP requests.
 *
 * The script expects the API URL as a command line argument (process.argv[2]).
 *
 * The 'request.get' function is used to make a GET request. It takes two arguments:
 * 1. The URL
 * 2. A callback function that is called when the HTTP request is complete.
 *
 * The callback function parses the response body as JSON, iterates over the todos, and maintains a count of completed tasks for each user in the 'allData' object.
 *
 * If a todo is not completed, it is skipped. If a todo is completed, the count for the user is incremented. If the user does not exist in 'allData', they are added with a count of 1.
 *
 * Finally, it logs the 'allData' object to the console.
 */
const request = require('request');
const url = process.argv[2];

request.get(url, (_, resp, body) => {
  const allData = {};
  const reqBody = JSON.parse(body);

  reqBody.forEach(todo => {
    if (todo.completed !== true) {
      return;
    }

    if (todo.userId in allData) {
      allData[`${todo.userId}`] = allData[`${todo.userId}`] + 1;
      return;
    }

    allData[`${todo.userId}`] = 1;
  });

  console.log(allData);
});
