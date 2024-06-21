#!/usr/bin/node
exports.converter = function (base) {
  function baseConverter (n) {
    if (n < base) {
      return String(n);
    } else {
      return baseConverter(Math.floor(n / base)) + String(n % base);
    }
  }

  return function (num) {
    return baseConverter(num);
  };
};
