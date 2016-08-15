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
