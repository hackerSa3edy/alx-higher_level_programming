#!/usr/bin/node

const lines = ['C', 'fun', 'Python', 'cool', 'JavaScript', 'amazing'];

let counter;
for (counter = 0; counter < lines.length; counter += 2) {
  console.log(`${lines[counter]} is ${lines[counter + 1]}`);
}
