#!/usr/bin/node
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    var ul = document.getElementById('list_movies');
    data.results.forEach(function (film) {
      var li = document.createElement('li');
      li.textContent = film.title;
      ul.appendChild(li);
    });
});