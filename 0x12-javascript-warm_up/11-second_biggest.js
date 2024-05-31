#!/usr/bin/node

let arrNumbers = process.argv.slice(2).map(Number);

function sortNumbers(arr) {
  return arr.sort((a, b) => a - b);
}

let sortedNumbers = sortNumbers(arrNumbers);

console.log(sortedNumbers[-2]);
