#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];

request.get(url+id, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const film = JSON.parse(body)
    for (let character of film.characters) {
        request(character, (err, res, body) => {
            if (err) {
                console.log(err);
            } else {
                console.log(JSON.parse(body).name)
            }
        })
    }
  }
});
