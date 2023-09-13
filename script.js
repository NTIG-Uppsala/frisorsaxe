document.addEventListener("DOMContentLoaded", function () {
  var hasjs = document.getElementsByClassName("hasjs");

  // Loop through each element with the class "hasjs"
  for (var i = 0; i < hasjs.length; i++) {
    hasjs[i].style.display = "block";
  }
});

var navBarOpen = false;

function navBarToggled() {
  navBarOpen = !navBarOpen;
}

var prevScrollPosition = window.pageYOffset;
window.onscroll = function () {
  if (navBarOpen === false) {
    var currScrolPosition = window.pageYOffset;
    if (prevScrollPosition > currScrolPosition) {
      document.getElementById("navbar").style.top = "0";
    } else {
      document.getElementById("navbar").style.top = "-20vh";
    }
    prevScrollPosition = currScrolPosition;
  }
};

function dailySales(date) {
  let weekday = date.getDay();
  const longHair = document.getElementsByClassName("longHair");
  const saleLongHair = document.getElementsByClassName("saleLongHair");
  const shortHair = document.getElementsByClassName("shortHair");
  const saleShortHair = document.getElementsByClassName("saleShortHair");
  const beard = document.getElementsByClassName("beard");
  const saleBeard = document.getElementsByClassName("saleBeard");
  const coloring = document.getElementsByClassName("coloring");
  const saleColoring = document.getElementsByClassName("saleColoring");

  switch (weekday) {
    case 1: //On Monday longhair is on sale
      for (const element of longHair) {
        element.style.textDecoration = "line-through";
      }
      for (const element of saleLongHair) {
        element.innerText = "Idag 540 kr ";
        element.style.color = "red";
      }
      break;
    case 2: //On Tuseday shorthair is on sale
      for (const element of shortHair) {
        element.style.textDecoration = "line-through";
      }
      for (const element of saleShortHair) {
        element.innerText = "Idag 180 kr ";
        element.style.color = "red";
      }
      break;
    case 3: //On Wednesday beard is on sale
      for (const element of beard) {
        element.style.textDecoration = "line-through";
      }
      for (const element of saleBeard) {
        element.innerText = "Idag 135 kr ";
        element.style.color = "red";
      }
      break;
    case 4: //On Thursday coloring is on sale
      for (const element of coloring) {
        element.style.textDecoration = "line-through";
      }
      for (const element of saleColoring) {
        element.innerText = "Idag 504 kr ";
        element.style.color = "red";
      }
      break;
  }
}
function changeFlag() {
  const lang = document.getElementById("language").lang;
  const en = document.getElementsByClassName("enMenu");
  const sv = document.getElementsByClassName("svMenu");

  if (lang === "en") {
    console.log("en");
  } else if (lang === "sv") {
    console.log("sv");
  }
}

function showFlags() {
  document.getElementById("activeMenu").style.display = "none";

  const languages = document.getElementsByClassName("inActiveMenu");

  //Show the langs that the user can select
  for (const element of languages) {
    element.style.display = "block";
  }
}
