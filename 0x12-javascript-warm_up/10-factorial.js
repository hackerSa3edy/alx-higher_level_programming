#!/usr/bin/node

const { argv } = require('process');

function factorial (n) {
  if (isNaN(n) || n <= 1) return 1;

  return factorial(n - 1) * n;
}

const result = factorial(Number(argv[2]));
console.log(result);
