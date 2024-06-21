#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let idx = 0;

  list.forEach(i => {
    if (i === searchElement) {
      idx++;
    }
  });

  return idx;
};
