#!/usr/bin/node

exports.xTimes = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
