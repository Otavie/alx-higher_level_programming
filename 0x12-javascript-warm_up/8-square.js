#!/usr/bin/node

const args = process.argv.slice(2);
const number = parseInt(args[0], 10);

let i = 0;

if (isNaN(number)) {
  console.log('Missing size');
} else {
  while (i < number) {
    console.log('X'.repeat(number));
    i++;
  }
}
