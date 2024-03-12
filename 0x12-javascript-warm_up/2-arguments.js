#!/usr/bin/node
const sz = process.argv.length;
let message;
if (sz === 2) {
  message = 'No argument';
} else if (sz === 3) {
  message = 'Argument found';
} else {
  message = 'Arguments found';
}
console.log(message);
