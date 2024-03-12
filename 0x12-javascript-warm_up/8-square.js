#!/usr/bin/node
const sz = parseInt(process.argv[2]);
if (isNaN(sz)) {
  console.log('Missing size');
} else if (sz > 0) {
  let square = '';
  for (let i = 0; i < sz; i++) {
    for (let j = 0; j < sz; j++) {
      square += 'X';
    }
    if (i !== sz - 1) {
      square += '\n';
    }
  }
  console.log(square);
}
