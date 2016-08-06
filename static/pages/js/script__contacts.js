var map = document.querySelector(".map");
var requisites = document.querySelector(".requisites");
var mapMask = map.querySelector(".map__mask");
var YANDEX_MAP_HEIGHT = 720;

requisites.appendChild(map);

map.style.background = "none";
map.style.width = "100%";
map.style.top = requisites.offsetHeight - YANDEX_MAP_HEIGHT + "px";
map.style.bottom = "0";
mapMask.style.display = "block";
