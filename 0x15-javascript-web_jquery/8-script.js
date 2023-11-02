$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const movies = data.results;
  const listItems = movies.map(movie => `<li>${movie.title}</li>`).join('');
  $('UL#list_movies').html(listItems);
});
