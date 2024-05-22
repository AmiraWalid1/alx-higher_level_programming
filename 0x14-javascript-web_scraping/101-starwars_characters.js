#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];

async function getCharacterName (characterUrl) {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

request.get(url + id, async (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const film = JSON.parse(body);
    for (const characterUrl of film.characters) {
      try {
        const characterName = await getCharacterName(characterUrl);
        console.log(characterName);
      } catch (error) {
        console.error(error);
      }
    }
  }
});
