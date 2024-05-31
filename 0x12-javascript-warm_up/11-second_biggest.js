#!/usr/bin/node

const arrs = process.argv.slice(2);
const arrNumbers = arrs.sort();

if (arrs.length <= 2) {
  console.log(0);
} else {
  console.log(arrNumbers[1]);
}
