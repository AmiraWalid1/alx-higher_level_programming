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
      if (film.characters.includes(url.slice(0, -5) + 'people/18/')) {
        cnt++;
      }
    }
    console.log(cnt);
  }
});
