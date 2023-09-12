#!/usr/bin/node

const arg = process.argv[2];
const x = parseInt(arg);

if (isNaN(x)) {
  console.log('Missing size');
}

for (let i = 0; i < x; i++) {
  let line = '';
  for (let j = 0; j < x; j++) {
    line += 'X';
  }
  console.log(line);
}
