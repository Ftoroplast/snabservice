"use strict";

(function () {
  var goods = document.querySelectorAll(".goods__element");

  [].forEach.call(goods, function (item, i, arr) {
    item.product_id = item.querySelector("input").getAttribute("name");

    item.metalType = item.parentElement.parentElement.parentElement.getAttribute("id");

    item.category = item.parentElement.parentElement.firstElementChild.innerHTML;

    item.amount = 0;

    var priceParameter = item.querySelector(".goods__parameter--price");
    item.price = parseInt(priceParameter.innerHTML);

    item.sum = 0;

    item.getAmount = function () {
      return this.amount;
    }

    item.setAmount = function (newValue) {
      this.amount = newValue;

      var amountParameter = this.querySelector("input");
      amountParameter.setAttribute("value", newValue);

      var sumParameter = this.querySelector(".goods__parameter--sum");
      if (newValue) {
        this.sum = newValue * this.price;
        sumParameter.innerHTML = this.sum;
      } else {
        sumParameter.innerHTML = "- - -";
      };

      addToCart(item);
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

  function addToCart(item) {
    var newCartItem = item.cloneNode(true);
    var inputAmount = newCartItem.querySelector("input");
    inputAmount.setAttribute("form", "form");
    newCartItem.setAmount = function (newValue) {
      item.setAmount(newValue);

      var amountParameterClone = this.querySelector("input");
      var amountParameterOriginal = item.querySelector("input");
      amountParameterClone.setAttribute("value", amountParameterOriginal.getAttribute("value"));

      var sumParameterClone = this.querySelector(".goods__parameter--sum");
      var sumParameterOriginal = item.querySelector(".goods__parameter--sum");
      sumParameterClone.innerHTML = sumParameterOriginal.innerHTML;
    }

    var cart = document.querySelector(".cart");
    var metalTypeCheckList = [];
    var categoryCheckList = [];
    var productIdCheckList = []
    if (!newCartItem.metalType in metalTypeCheckList) {
      metalTypeCheckList.push(newCartItem.metalType);
      productIdCheckList.push(newCartItem.product_id);

      addNewItemToTable(createNewTable());
    } else if (!newCartItem.category in categoryCheckList) {
      categoryCheckList.push(newCartItem.category);
      productIdCheckList.push(newCartItem.product_id);

      addNewItemToTable(createNewTable());
    } else if (!newCartItem.product_id in productIdCheckList) {
      var captions = cart.querySelectorAll("caption");
      var requireCaption = newCartItem.metalType + " " + newCartItem.category;
      [].forEach.call(captions, function (caption, i, arr) {
        if (caption.innerHTML == requireCaption) {
          addNewItemToTable(caption.nextElement);
        }
      })
    }

    function createNewTable() {
      var newTable = item.parentElement.parentElement.cloneNode(true);
      var newTableBody = newTable.querySelector("tbody");
      var newTableBodyElements = newTableBody.querySelectorAll(".goods__element");
      [].forEach.call(newTableBodyElements, function (newTableBodyElement, i, arr) {
        arr.removeChild(newTableBodyElement);
      });
      var newTableCaption = newTable.querySelector("caption");
      newTableCaption.innerHTML = newCartItem.metalType + " " + newCartItem.category;
      cart.appendChild(newTable);

      return newTableBody;
    }

    function addNewItemToTable(tableBody) {
      tableBody.appendChild(newCartItem);
    }
  }
})();
