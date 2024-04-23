#!/usr/bin/node
/**
 * This script reads a file and prints its content to the console.
 *
 * It uses Node.js built-in modules: 'fs' for file system operations and 'process' for accessing system information.
 *
 * The script expects a file path as a command line argument (process.argv[2]).
 *
 * The 'fs.readFile' function is used to read the file. It takes three arguments:
 * 1. The file path
 * 2. The file encoding ('utf-8' in this case)
 * 3. A callback function that is called when the file read operation is complete.
 *
 * The callback function checks if there was an error during the file read operation.
 * If there was an error, it logs the error to the console and returns.
 * If there was no error, it logs the file content to the console.
 */

const fs = require('fs');
const process = require('process');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, buffer) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(buffer);
});
