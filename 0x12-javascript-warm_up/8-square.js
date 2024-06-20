#!/usr/bin/node

const cmdArgs = process.argv.slice(2);
let i = 1;
let j = 1;
if (cmdArgs[0] === undefined || isNaN(cmdArgs)) {
  console.log('Missing size');
} else {
  for (i = 0; i < cmdArgs[0]; i++) {
    let row = '';
    for (j = 0; j < cmdArgs[0]; j++) {
      row+= 'X';
    }
  console.log(row);
  }
}
