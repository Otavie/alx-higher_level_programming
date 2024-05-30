#!/usr/bin/node

// Get the arguments passed to the script
const args = process.argv.slice(2);

const number = parseInt(args[0], 10);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
