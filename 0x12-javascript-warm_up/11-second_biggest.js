#!/usr/bin/node

const arrs = process.argv.slice(2);
const arrNumbers = arrs.sort().reverse();

if (arrNumbers.length <= 1) {
  console.log(0);
} else {
  console.log(arrNumbers[1]);
}
