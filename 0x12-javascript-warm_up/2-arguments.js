#!/usr/bin/node

// Fet the arguments passed to the script
const cmdArgs = process.argv.slice(2);

if (cmdArgs == 0) {
	console.log('No argument');
} else if (cmdArgs = 1) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
