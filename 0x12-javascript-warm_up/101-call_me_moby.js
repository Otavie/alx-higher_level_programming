#!/usr/bin/node

module.exports = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
