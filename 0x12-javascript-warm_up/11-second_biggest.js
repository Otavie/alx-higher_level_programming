#!/usr/bin/node

let arrs = process.argv.slice(2);
let arrNumbers = arrs.map(Number);

arrNumbers.sort((a, b) => b - a);

if (arrs.length === 0) {
  console.log(0);
} else if (arrs.length === 1) {
  console.log(1);
} else {
  console.log(arrNumbers[1]);
}
