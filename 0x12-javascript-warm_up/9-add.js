#!/usr/bin/node

// Fetch the arguments passed to the script
const cmdArgs = process.argv.slice(2);
const arg1 = parseInt(cmdArgs[0]);
const arg2 = parseInt(cmdArgs[1]);

function add (a, b) {
  return (a + b);
}

console.log(add(arg1, arg2));
