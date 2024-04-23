#!/usr/bin/node
/**
 * This script writes content to a file.
 *
 * It uses Node.js built-in modules: 'fs' for file system operations and 'process' for accessing system information.
 *
 * The script expects two command line arguments (process.argv[2] and process.argv[3]):
 * 1. The file path where the content will be written.
 * 2. The content to be written to the file.
 *
 * The 'fs.writeFile' function is used to write the content to the file. It takes four arguments:
 * 1. The file path
 * 2. The content to be written
 * 3. The file encoding ('utf-8' in this case)
 * 4. A callback function that is called when the file write operation is complete.
 *
 * The callback function checks if there was an error during the file write operation.
 * If there was an error, it logs the error to the console and returns.
 */

const fs = require('fs');
const process = require('process');
const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', (err, buffer) => {
  if (err) {
    console.error(err);
  }
});
