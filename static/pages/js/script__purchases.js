(function () {
  var categories = document.querySelectorAll(".requirements__parameter--category");
  [].forEach.call(categories, function (category, i, arr) {
    var innerWrapper = document.createElement("div");
    innerWrapper.className = "jsInnerWrapper";
    innerWrapper.innerHTML = category.innerHTML;
    category.innerHTML = "";
    category.appendChild(innerWrapper);
  });
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
    [].forEach.call(categories, function (category, i, arr) {
      var innerWrapper = category.querySelector(".jsInnerWrapper");
      var CATEGORY_PADDING = 40;
      var TOP_STOP_DISTANCE = getCoords(category).top - header.offsetHeight;
      var BOTTOM_STOP_DISTANCE = getCoords(category).top + category.offsetHeight - header.offsetHeight - innerWrapper.offsetHeight - 2 * CATEGORY_PADDING;
      if (pageYOffset >= TOP_STOP_DISTANCE
          && pageYOffset < BOTTOM_STOP_DISTANCE
          && !innerWrapper.classList.contains("jsFixed")) {
        innerWrapper.style.marginTop = "0";
        innerWrapper.style.top = getCoords(innerWrapper).top - getCoords(category).top + header.offsetHeight + "px";
        innerWrapper.style.left = getCoords(innerWrapper).left + "px";
        innerWrapper.classList.add("jsFixed");
      } else if ((pageYOffset >= BOTTOM_STOP_DISTANCE
                  || pageYOffset < TOP_STOP_DISTANCE)
                  && innerWrapper.classList.contains("jsFixed")) {
        innerWrapper.classList.remove("jsFixed");
        if (pageYOffset >= BOTTOM_STOP_DISTANCE) {
          innerWrapper.style.marginTop = BOTTOM_STOP_DISTANCE - TOP_STOP_DISTANCE + "px";
        } else if (pageYOffset <= TOP_STOP_DISTANCE) {
          innerWrapper.style.marginTop = "0";
        }
      }
    })
    if (pageYOffset === 0) {
      header.uncompress();
    } else {
      header.compress();
    }
  }

  var purchasesForm = document.querySelector(".form-section__form--order");
  var fileLabel = purchasesForm.querySelector(".form__label--documents");
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
          case "mpeg4":
          case "avi":
          case "3gp":
            var video = document.createElement("div");
            video.className = "form__icon form__icon--video";
            fileLabel.appendChild(video);
            if (uploadedFile.name.length > MAX_FILE_NAME_CHARACTERS) {
              video.innerHTML = uploadedFile.name.slice(0, MAX_FILE_NAME_CHARACTERS) + "...";
            } else {
              video.innerHTML = uploadedFile.name;
            }
            break;
          }
        if (countOfUploadedFiles < MAX_FILES_COUNT) {
          var cloneFileLabel = fileLabel.cloneNode(true);
          fileLabel.classList.add("jsHide");
          purchasesForm.insertBefore(cloneFileLabel, fileLabel);
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

  function getCoords(elem) { // кроме IE8-
    var box = elem.getBoundingClientRect();

    return {
      top: box.top + pageYOffset,
      left: box.left + pageXOffset
    };
  }
})();
