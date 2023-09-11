#!/usr/bin/node

const argsNumber = process.argv.length;

if (argsNumber === 2) {
  console.log('No argument');
} else if (argsNumber === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
