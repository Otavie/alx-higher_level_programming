#!/usr/bin/node
exports.converter = function (base) {
  function baseConverter (n) {
    if (n < base) {
      if (base === 16 && n >= 10 && n <= 15) {
        return String.fromCharCode(n + 87);
      } else {
        return String(n);
      }
    } else {
      return baseConverter(Math.floor(n / base)) + String(n % base);
    }
  }

  return function (num) {
    return baseConverter(num);
  };
};
