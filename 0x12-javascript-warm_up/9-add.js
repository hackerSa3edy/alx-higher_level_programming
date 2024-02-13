#!/usr/bin/node

const { argv } = require('process');
const fNum = Number(argv[2]);
const sNum = Number(argv[3]);

function add (a, b) {
  console.log(fNum + sNum);
}

add(fNum, sNum);
