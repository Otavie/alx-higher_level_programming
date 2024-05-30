#!/usr/bin/node

const args = process.argv.slice(2);
const number = parseInt(args[0], 10);

let i = 0;

if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  while (i < number) {
    console.log('C is fun');
    i++;
  }
}
