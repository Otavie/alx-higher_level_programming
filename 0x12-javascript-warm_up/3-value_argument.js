#!/usr/bin/node

// Fetch the arguments passed to the script
const cmdArgs = process.argv.slice(2);
let count = 0;

for (const cmdArg of cmdArgs) { count++; }

if (count === 0) {
  console.log('No argument');
} else {
  console.log(cmdArgs[0]);
}
