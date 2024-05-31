#!/usr/bin/node

const numbers = process.argv.slice(2).map(Number);
const sortedNumbers = numbers.sort((a, b) => b - a);

if (sortedNumbers.length <= 1) {
  console.log(0);
} else {
  console.log(sortedNumbers[1]);
}
