#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error.message);
  } else {
    try {
      const movieData = JSON.parse(body);
      const charactersUrls = movieData.characters;

      const printCharacterNames = async () => {
        for (const characterUrl of charactersUrls) {
          const characterResponse = await new Promise((resolve, reject) => {
            request.get(characterUrl, (error, response, body) => {
              if (error) {
                reject(error);
              } else {
                resolve(body);
              }
            });
          });
          const characterData = JSON.parse(characterResponse);
          console.log(characterData.name);
        }
      };

      printCharacterNames();
    } catch (parseError) {
      console.error(parseError.message);
    }
  }
});
