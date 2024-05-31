#!/usr/bin/node

const arrs = process.argv.slice(2);
const arrNumbers = arrs.sort();

if (arrNumbers.length <= 1) {
  console.log(0);
} else {
  console.log(arrNumbers[arrNumbers.length - 2]);
}
