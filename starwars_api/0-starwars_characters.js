#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(filmUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const characters = JSON.parse(body).characters;
  printCharactor(characters, 0);
});

function printCharactor (characters, index) {
  if (index >= characters.length) {
    return;
  }
  request(characters[index], (error, response, body) => {
    if (!error) {
      console.log(JSON.parse(body).name);
    }
    printCharactor(characters, index + 1);
  });
}
