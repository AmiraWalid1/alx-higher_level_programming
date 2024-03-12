#!/usr/bin/node
let arg = process.argv[2];
if (arg === undefined) {
  arg = 'No argument';
}
console.log(arg);
