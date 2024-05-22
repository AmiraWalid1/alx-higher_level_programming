#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let wedgeAntilles = '';
for (const i in url) {
  if (url.substr(i, 4) === '/api') {
    wedgeAntilles += url.substr(i, 4);
    break;
  } else {
    wedgeAntilles += url[i];
  }
}

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    let cnt = 0;
    const films = JSON.parse(body).results;
    for (const film of films) {
      if (film.characters.includes(wedgeAntilles + '/people/18/')) {
        cnt++;
      }
    }
    console.log(cnt);
  }
});
