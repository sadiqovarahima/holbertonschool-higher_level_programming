#!/usr/bin/node
document.getElementById('add_item').addEventListener('click', function () {
    var ul = document.querySelector('ul.my_list');
    var li = document.createElement('li');
    li.textContent = 'Item';
    ul.appendChild(li);
});