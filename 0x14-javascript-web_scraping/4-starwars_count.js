#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/';

request.get(url + 'films/', (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    let cnt = 0;
    const films = JSON.parse(body).results;
    for (const film of films) {
      if (film.characters.includes(url + 'people/18/')) {
        cnt++;
      }
    }
    console.log(cnt);
  }
});
