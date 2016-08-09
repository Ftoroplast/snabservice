// var introduction = document.querySelector(".introduction");
// var header = document.querySelector("header");
// var zoom = screen.deviceXDPI / screen.logicalXDPI;
// var introductionP = introduction.querySelectorAll("p");
// var introductionH = introduction.querySelector("h1");
// var introductionA = introduction.querySelector("a");
// var introductionLogo = introduction.querySelector(".partner__logo");
//
// setInterval(function () {
//   if (introduction.offsetWidth >= 1200) {
//     var lastScaleValue = getComputedStyle(introduction).transform;
//     introduction.style.transform = "scale(" + (screen.height - header.offsetHeight)/(introduction.offsetHeight) + ")";
//     var lastMargin = getComputedStyle(introduction).marginBottom;
//     introduction.style.marginBottom = introduction.offsetHeight * (parseFloat(getComputedStyle(introduction).transform.slice(7, 10)) - 1) + "px";
//   } else {
//     introduction.style.transform = lastScaleValue;
//     introduction.style.marginBottom = lastMargin + "px";
//   }
//
//   [].forEach.call(introductionP, function (item, i, arr) {
//     item.style.transform = "scale(" + (introduction.offsetHeight)/(screen.height - header.offsetHeight)+ ")";
//   });
//
//   introductionH.style.transform = "scale(" + (introduction.offsetHeight)/(screen.height - header.offsetHeight) + ")";
//
//   introductionA.style.transform = "scale(" + (introduction.offsetHeight)/(screen.height - header.offsetHeight) + ")";
//
//   introductionLogo.style.transform = "scale(" + (introduction.offsetHeight)/(screen.height - header.offsetHeight) + ")";
// }, 100);
