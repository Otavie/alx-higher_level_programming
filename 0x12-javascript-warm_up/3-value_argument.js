#!/usr/bin/node

// Fetch the arguments passed to the script
const cmdArgs = process.argv.slice(2);

if (cmdArgs[0] === undefined) {
  console.log('No argument');
} else {
  console.log(cmdArgs[0]);
}
