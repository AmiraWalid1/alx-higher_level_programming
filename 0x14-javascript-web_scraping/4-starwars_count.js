#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    let cnt = 0;
    const films = JSON.parse(body).results;
    for (const film of films) {
      cnt += (film.characters.find(character => character.endsWith('/18/'))) ? 1 : 0;
    }
    console.log(cnt);
  }
});
