#!/usr/bin/node

const { argv } = require('process');
const sortedArray = argv.slice(2).sort((a, b) => a - b);
const arrLength = sortedArray.length;

if (arrLength <= 1) console.log(0);
else {
  console.log(sortedArray[arrLength - 2]);
}
