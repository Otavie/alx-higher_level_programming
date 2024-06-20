#!/usr/bin/node

// Fetch the arguments passed to the script
const cmdArgs = process.argv.slice(2);
const arrNumbers = cmdArgs.sort((a, b) => a - b);

if (arrNumbers.length <= 1) {
  console.log(0);
} else {
  console.log(arrNumbers[arrNumbers.length - 2]);
}
