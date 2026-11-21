#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(filmUrl, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    return;
  }

  const film = JSON.parse(body);
  const characterUrls = film.characters || [];
  const names = new Array(characterUrls.length);
  let completed = 0;

  if (characterUrls.length === 0) {
    return;
  }

  characterUrls.forEach((url, index) => {
    request(url, (charError, charResponse, charBody) => {
      if (!charError && charResponse.statusCode === 200) {
        names[index] = JSON.parse(charBody).name;
      }
      completed += 1;
      if (completed === characterUrls.length) {
        names.forEach((name) => {
          if (name) {
            console.log(name);
          }
        });
      }
    });
  });
});
