#!/usr/bin/node
const fs = require('fs');
const fileName = process.argv[2];
const data = process.argv[3];
fs.writeFile(fileName, data, 'utf8', err => {
  if (err) {
    console.log(err);
  }
});
