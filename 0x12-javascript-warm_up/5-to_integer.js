#!/usr/bin/node

// Fetch the arguments passed to the script
const cmdArgs = process.argv.slice(2);
if (isNaN(parseInt(cmdArgs[0]))) {
  console.log('Not a number');
} else {
  console.log(parseInt(cmdArgs[0]));
}
