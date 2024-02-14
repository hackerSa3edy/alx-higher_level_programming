#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let char = '';
    for (let counter = 0; counter < this.width; counter++) char += 'X';

    for (let counter = 0; counter < this.height; counter++) console.log(char);
  }
}

module.exports = Rectangle;
