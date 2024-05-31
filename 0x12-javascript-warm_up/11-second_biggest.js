#!/usr/bin/node

let arrs = process.argv.slice(2);
let arrNumbers = arrs.map(Number);

function sortNumbers(arr) {
  return arr.sort((a, b) => a - b);
}

let sortedNumbers = sortNumbers(arrNumbers);

if (arrs.length === 0) {
  console.log(0);
} else if (arrs.length === 1) {
  console.log(1);
} else {
  console.log(sortedNumbers[sortedNumbers.length - 2]);
}
