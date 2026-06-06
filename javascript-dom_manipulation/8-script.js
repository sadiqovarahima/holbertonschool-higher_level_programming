#!/usr/bin/node
document.addEventListener('DOMContentLoaded', function () {
    fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        document.getElementById('hello').textContent = data.hello;
      });
});