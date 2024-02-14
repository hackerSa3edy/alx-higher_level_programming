#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];
  for (let counter = list.length - 1; counter >= 0; counter--) reversed.push(list[counter]);

  return reversed;
};
