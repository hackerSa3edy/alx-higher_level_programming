$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    dataType: 'json',
    success: function (response) {
      const movies = response.results.map(result => `<li>${result.title}</li>`);
      $('ul#list_movies').html(movies);
      // console.log(movies);
    }
  });
});
