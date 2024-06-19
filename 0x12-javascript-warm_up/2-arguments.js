#!/usr/bin/node

// Fetch the arguments passed to the script
const cmdArgs = process.argv.slice(2);

if (cmdArgs.length === 0) {
    console.log('No argument');
} else if (cmdArgs.length === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
