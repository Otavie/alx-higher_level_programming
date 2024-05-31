#!/usr/bin/node

function factorial(n) {
  if(NaN(n) || n === 0) {
    return 0;
  } else  {
    return n * factorial (n - 1);
  }
}
console.log(parseInt(process.argv[2]));
