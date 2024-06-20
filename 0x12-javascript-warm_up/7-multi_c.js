#!/usr/bin/node

const cmdArgs = process.argv.slice(2);
let i = 1;
if (cmdArgs[0] === undefined) {
  console.log('Missing number of occurrences');
} else {
  while (i <= cmdArgs[0]) {
    console.log('C is fun');
    i++;
  }
}
