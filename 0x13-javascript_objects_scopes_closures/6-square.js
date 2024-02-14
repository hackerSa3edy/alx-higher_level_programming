#!/usr/bin/node

const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c = 'X') {
    let char = '';

    for (let counter = 0; counter < this.width; counter++) char += c;

    for (let counter = 0; counter < this.height; counter++) console.log(char);
  }
}

module.exports = Square;
