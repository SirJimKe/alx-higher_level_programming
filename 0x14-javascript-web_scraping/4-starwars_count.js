#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

const characterId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error.message);
  } else {
    try {
      const movieData = JSON.parse(body);
      const wedgeAntillesMovies = movieData.results.filter(movie =>
        movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
      );
      console.log(wedgeAntillesMovies.length);
    } catch (parseError) {
      console.error(parseError.message);
    }
  }
});
