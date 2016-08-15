var map = document.querySelector(".map");
var requisites = document.querySelector(".requisites");
var mapMask = map.querySelector(".map__mask");
var YANDEX_MAP_HEIGHT = 720;
var MAP_MARGIN_LEFT = 700;

requisites.appendChild(map);

map.style.background = "none";
map.style.width = "100%";
map.style.top = requisites.offsetHeight - YANDEX_MAP_HEIGHT + "px";
map.style.bottom = "0";
var zoomIndicator = document.body.offsetWidth;
setInterval(function () {
  if (document.body.offsetWidth !== zoomIndicator) {
    map.style.left = getCoords(requisites.querySelector(".container")).left + MAP_MARGIN_LEFT +"px";
    zoomIndicator = document.body.offsetWidth;
  }
}, 100);
mapMask.style.display = "block";

var header = document.querySelector("header");
header.compress = function () {
  if (!this.classList.contains("header--compact")) {
    this.classList.add("header--compact");
  }
};
header.uncompress = function () {
  if (this.classList.contains("header--compact")) {
    this.classList.remove("header--compact");
  }
};

window.onscroll = function (e) {
  if (pageYOffset === 0) {
    header.uncompress();
  } else {
    header.compress();
  }
}

function getCoords(elem) { // кроме IE8-
  var box = elem.getBoundingClientRect();

  return {
    top: box.top + pageYOffset,
    left: box.left + pageXOffset
  };
}
