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

var vacanciesForm = document.querySelector(".form-section__form--application");
var fileLabel = vacanciesForm.querySelector(".form__label--documents");
var fileInput = fileLabel.querySelector(".form__input--documents");
var countOfUploadedFiles = 0;
fileInput.onchange = function (e) {
  var uploadedFiles = this.files;
  countOfUploadedFiles += uploadedFiles.length;
  var MAX_FILES_COUNT = 2;
  var MAX_FILE_NAME_CHARACTERS = 20;
  if (countOfUploadedFiles <= MAX_FILES_COUNT) {
    [].forEach.call(uploadedFiles, function (uploadedFile, i, arr) {
      switch (uploadedFile.name.split(".")[uploadedFile.name.split(".").length - 1]) {
        case "png":
        case "jpg":
          var image = document.createElement("div");
          image.className = "form__icon form__icon--image";
          fileLabel.appendChild(image);
          if (uploadedFile.name.length > MAX_FILE_NAME_CHARACTERS) {
            image.innerHTML = uploadedFile.name.slice(0, MAX_FILE_NAME_CHARACTERS) + "...";
          } else {
            image.innerHTML = uploadedFile.name;
          }
          break;
        case "doc":
        case "docx":
        case "zip":
        case "pdf":
          var application = document.createElement("div");
          application.className = "form__icon form__icon--application";
          fileLabel.appendChild(application);
          if (uploadedFile.name.length > MAX_FILE_NAME_CHARACTERS) {
            application.innerHTML = uploadedFile.name.slice(0, MAX_FILE_NAME_CHARACTERS) + "...";
          } else {
            application.innerHTML = uploadedFile.name;
          }
          break;
        }
      if (countOfUploadedFiles < MAX_FILES_COUNT) {
        var cloneFileLabel = fileLabel.cloneNode(true);
        fileLabel.classList.add("jsHide");
        vacanciesForm.insertBefore(cloneFileLabel, fileLabel);
        fileLabel = cloneFileLabel;
        var cloneFileInput = cloneFileLabel.querySelector(".form__input--documents");
        cloneFileInput.setAttribute("name", "document" + (i + 2));
        cloneFileInput.onchange = fileInput.onchange;
      } else {
        fileLabel.onclick = function (e) {
          alert("Нельзя загрузить больше " + MAX_FILES_COUNT + " файлов");

          return false;
        }
      }
    });
  } else {
    alert("Нельзя загрузить больше " + MAX_FILES_COUNT + " файлов");
  }
}
