#!/usr/bin/node

// Fetch the arguments passed to the script
const cmdArgs = process.argv.slice(2);
const arg1 = parseInt(cmdArgs[0]);

function factorial (n) {
  if (n === 1) {
    return 1;
  } else if (n > 1) {
    return (n * factorial(n - 1));
  }
}

if (isNaN(arg1)) {
  console.log(1);
} else {
  console.log(factorial(arg1));
}
