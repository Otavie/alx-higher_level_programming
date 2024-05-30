#!/usr/bin/node

const args = process.argv.slice(2);
const args1 = parseInt(args[0], 10);
const args2 = parseInt(args[1], 10);

function add (a, b) {
  console.log(a + b);
}

if (isNaN(args1)|| isNaN(args2)) {
  console.log('NaN');
} else {
  add(args1, args2);
}
