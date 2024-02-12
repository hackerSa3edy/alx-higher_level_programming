#!/usr/bin/node

const { argv } = require('process');

const isNumber = Number(argv[2]);
if (isNaN(isNumber)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${argv[2]}`);
}
