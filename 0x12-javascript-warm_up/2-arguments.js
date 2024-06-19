#!/usr/bin/node

// Fet the arguments passed to the script
const cmdArgs = process.argv.slice(2);

if (cmdArgs.length === 0) {
	console.log('No argument');
} else if (cmdArgs.length === 1) {
	console.log('Argument found');
} else if (cmdArgs.length > 1) {
	console.log('Arguments found');
}
