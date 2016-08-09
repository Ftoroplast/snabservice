"use strict";

(function () {
  var goods = document.querySelectorAll(".goods__element");

  [].forEach.call(goods, function (item, i, arr) {
    item.product_id = i;

    item.metalType = item.parentElement.parentElement.parentElement.getAttribute("id");

    item.category = item.parentElement.parentElement.firstElementChild.innerHTML;

    var amountParameter = item.querySelector("input");

    item.getAmount = function () {
      return parseInt(amountParameter.getAttribute("value"));
    }

    item.setAmount = function (newValue) {
      amountParameter.setAttribute("value", newValue);

      var sumParameter = this.querySelector(".goods__parameter--sum");
      if (newValue) {
        sumParameter.innerHTML = newValue * parseInt(this.querySelector(".goods__parameter--price").innerHTML) + " Р";

        cart.addItem(this);
      } else {
        sumParameter.innerHTML = "- - -";

        cart.removeItem(item);
      };
    }

    var increaseArrow = item.querySelector(".goods__arrow--up");
    increaseArrow.onclick = function () {
      var newValue = item.getAmount() + 1;
      item.setAmount(newValue);
    };

    var decreaseArrow = item.querySelector(".goods__arrow--down");
    decreaseArrow.onclick = function () {
      if (item.getAmount() > 0) {
        var newValue = item.getAmount() - 1;
        item.setAmount(newValue);
      };
    }
  });

  var cart = document.querySelector(".cart");

  cart.__findItem = function (item) {
    var cartItems = cart.querySelectorAll(".goods__element");
    for (var i = 0; i < cartItems.length; ++i) {
      if (item.product_id == cartItems[i].product_id) {
        return cartItems[i];
      }
    };
  }

  cart.__findTable = function (item) {
    var cartTables = document.querySelectorAll(".goods__table");
    var searchableTableCaption = item.metalType + " " + item.category;
    for (var i = 0; i < cartTables.length; ++i) {
      if (searchableTableCaption == cartTables[i].querySelector("caption").innerHTML) {
        return cartTables[i];
      }
    };
  }

  cart.__createTable = function (item) {
    var newTable = item.parentElement.parentElement.cloneNode(true);
    var newTableBody = newTable.querySelector("tbody");
    var newTableElements = newTable.querySelectorAll(".goods__element");
    [].forEach.call(newTableElements, function (newTableElement, i, arr) {
      newTableBody.removeChild(newTableElement);
    });
    var newTableCaption = newTable.querySelector("caption");
    newTableCaption.innerHTML = item.metalType + " " + item.category;
    cart.appendChild(newTable);

    return newTable;
  }

  cart.addItem = function (item) {
    var cartItem = item.cloneNode(true);
    cartItem.product_id = item.product_id;
    cartItem.metalType = item.metalType;
    cartItem.category = item.category;
    cartItem.querySelector("input").setAttribute("form", "form");

    if (item.metalType === "Арматура") {
      var shapeParameter = cartItem.querySelector(".goods__parameter--shape");
      if (shapeParameter) {
        shapeParameter.setAttribute("rowspan", "1");
      } else {
        var previousElement = item.previousElementSibling;
        while (!previousElement.querySelector(".goods__parameter--shape")) {
          previousElement = previousElement.previousElementSibling;
        }
        shapeParameter = document.createElement("td");
        shapeParameter.className = "goods__parameter goods__parameter--shape";
        cartItem.insertBefore(shapeParameter, cartItem.querySelector(".goods__parameter--diameter"));
        shapeParameter.innerHTML = previousElement.querySelector(".goods__parameter--shape").innerHTML;
      }
    }

    var amountParameter = cartItem.querySelector("input");
    cartItem.getAmount = function () {
      return parseInt(amountParameter.getAttribute("value"));
    }

    cartItem.setAmount = function (newValue) {
      amountParameter.setAttribute("value", newValue);

      var sumParameter = this.querySelector(".goods__parameter--sum");
      if (newValue) {
        sumParameter.innerHTML = newValue * parseInt(this.querySelector(".goods__parameter--price").innerHTML) + " Р";
      } else {
        sumParameter.innerHTML = "- - -";
      };

      var amountParameterClone = this.querySelector("input");
      var amountParameterOriginal = item.querySelector("input");
      amountParameterOriginal.setAttribute("value", amountParameterClone.getAttribute("value"));

      var sumParameterClone = this.querySelector(".goods__parameter--sum");
      var sumParameterOriginal = item.querySelector(".goods__parameter--sum");
      sumParameterOriginal.innerHTML = sumParameterClone.innerHTML;

      if (!this.getAmount()) {
        cart.removeItem(this);
      }
    }

    var increaseArrow = cartItem.querySelector(".goods__arrow--up");
    increaseArrow.onclick = function () {
      var newValue = cartItem.getAmount() + 1;
      cartItem.setAmount(newValue);
    };

    var decreaseArrow = cartItem.querySelector(".goods__arrow--down");
    decreaseArrow.onclick = function () {
      if (cartItem.getAmount() > 0) {
        var newValue = cartItem.getAmount() - 1;
        cartItem.setAmount(newValue);
      };
    }

    if (this.__findItem(item)) {
      console.log("OK");
      this.__findItem(item).setAmount(item.getAmount());
    } else if (this.__findTable(item)) {
      this.__findTable(item).querySelector("tbody").appendChild(cartItem);
    } else {
      console.log(this.__findItem(item));
      this.__createTable(item).querySelector("tbody").appendChild(cartItem);
    }
  }

  cart.removeItem = function (item) {
    if (this.__findItem(item).parentElement.children.length < 3) {
      this.__findTable(item).parentElement.removeChild(this.__findTable(item));
    } else {
      this.__findItem(item).parentElement.removeChild(this.__findItem(item));
    }
  }

  var stationLabel = document.querySelector(".form__label--station");
  stationLabel.show = show;
  stationLabel.hide = hide;

  var addressLabel = document.querySelector(".form__label--address");
  addressLabel.show = show;
  addressLabel.hide = hide;

  function show() {
    if (!this.classList.contains("jsShow")) {
      this.classList.addClass("jsShow");
    }
  };

  function hide() {
    if (this.classList.contains("jsShow")) {
      this.classList.removeClass("jsShow");
    }
  };

  var deliveryTypeSelect = document.querySelector(".form__input--delivery");
  var deliveryTypeOptions = deliveryTypeSelect.querySelectorAll("option");
  var deliveryTypeOptionFlag = "";
  [].forEach.call(deliveryTypeOptions, function (deliveryTypeOption, i, arr) {
    deliveryTypeOption.onclick = function () {
      deliveryTypeOptionFlag = deliveryTypeOption.getAttribute("value");
    };
  })
  deliveryTypeSelect.onchange = function () {
    if (deliveryTypeOptionFlag == "Железной дорогой") {
      console.log("1");
      addressLabel.hide();
      stationLabel.show();
    } else if (deliveryTypeOptionFlag == "Автотранспортом") {
      stationLabel.hide();
      addressLabel.show();
    } else {
      addressLabel.hide();
      stationLabel.hide();
    }
  }
})();
