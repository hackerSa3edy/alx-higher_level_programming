#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let dup = 0;

  list.forEach(element => {
    if (element === searchElement) dup++;
  });

  return dup;
};
