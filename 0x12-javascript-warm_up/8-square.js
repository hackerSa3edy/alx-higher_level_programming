#!/usr/bin/node

const { argv } = require('process');
let char = '';
const sqSize = Number(argv[2]);

for (let width = 0; width < sqSize; width++) {
  char += 'X';
}

if (!isNaN(sqSize)) {
  for (let height = 0; height < sqSize; height++) {
    console.log(char);
  }
} else {
  console.log('Missing size');
}
