#!/usr/bin/node

const { argv } = require('process');
const statement = 'C is fun';
const xTimes = Number(argv[2]);

if (!isNaN(xTimes)) {
  for (let counter = 0; counter < xTimes; counter++) {
    console.log(statement);
  }
} else {
  console.log('Missing number of occurrences');
}
