//Displays all elemnt with class name "hasjs"
document.addEventListener("DOMContentLoaded", function () {
  let hasjs = document.getElementsByClassName("hasjs");

  // Loop through each element with the class "hasjs"
  for (let i = 0; i < hasjs.length; i++) {
    hasjs[i].style.display = "block"; //Block shows element
  }
});

var navBarOpen = false;

function navBarToggled() {
  navBarOpen = !navBarOpen; //If called it will switch the variable, if true to false and if false to true
}

// Store the previous scroll position
var prevScrollPosition = window.scrollY;

//Hides the navbar when scrolling down, shows when scrolling up.
window.onscroll = function () {
  //Will not hide navbar if its active on smaller screen
  if (navBarOpen === false) {
    let currentScrollPosition = window.scrollY;
    // Compare scroll positions to show or hide the navbar
    if (currentScrollPosition === 0) {
      document.getElementById("navbar").style.top = "0";
    } else if (prevScrollPosition > currentScrollPosition) {
      document.getElementById("navbar").style.top = "0";
    } else {
      document.getElementById("navbar").style.top = "-20vh";
    }
    // Update the previous scroll position
    prevScrollPosition = currentScrollPosition;
  }
};

function dailySales(date) {
  const lang = document.getElementById("language").lang;

  const openHours = {
    kiruna: {
      weekdayOpen: 10,
      mondayClose: 16,
      tuesdayClose: 16,
      wednesdayClose: 16,
      thursdayClose: 16,
    },
    lulea: {
      weekdayOpen: 10,
      mondayClose: 17,
      tuesdayClose: 16,
      wednesdayClose: 15,
      thursdayClose: 16,
    },
  };

  //variable is dependent on the url, includes check if the url containts a word
  const locationOpeningHours = window.location.pathname.includes("lulea")
    ? openHours.lulea
    : window.location.pathname.includes("kiruna")
    ? openHours.kiruna
    : console.log("location does not have openingHours for dailysailes");

  const weekday = date.getDay();
  const hour = date.getHours();
  const longHair = document.getElementsByClassName("longHair");
  const saleLongHair = document.getElementsByClassName("saleLongHair");
  const shortHair = document.getElementsByClassName("shortHair");
  const saleShortHair = document.getElementsByClassName("saleShortHair");
  const beard = document.getElementsByClassName("beard");
  const saleBeard = document.getElementsByClassName("saleBeard");
  const coloring = document.getElementsByClassName("coloring");
  const saleColoring = document.getElementsByClassName("saleColoring");

  // Check the language and set the text accordingly
  const todayText = lang === "en" ? "Today" : "Idag";

  switch (weekday) {
    case 1: //On Monday longhair is on sale
      if (
        hour >= locationOpeningHours.weekdayOpen &&
        locationOpeningHours.mondayClose > hour
      ) {
        for (const element of longHair) {
          element.style.textDecoration = "line-through";
        }
        for (const element of saleLongHair) {
          element.innerText = `${todayText} 540 kr `;
          element.style.color = "red";
        }
      }
      break;
    case 2: //On Tuesday shorthair is on sale
      if (
        hour >= locationOpeningHours.weekdayOpen &&
        locationOpeningHours.tuesdayClose > hour
      ) {
        for (const element of shortHair) {
          element.style.textDecoration = "line-through";
        }
        for (const element of saleShortHair) {
          element.innerText = `${todayText} 180 kr `;
          element.style.color = "red";
        }
      }
      break;
    case 3: //On Wednesday beard is on sale
      if (
        hour >= locationOpeningHours.weekdayOpen &&
        locationOpeningHours.wednesdayClose > hour
      ) {
        for (const element of beard) {
          element.style.textDecoration = "line-through";
        }
        for (const element of saleBeard) {
          element.innerText = `${todayText} 135 kr `;
          element.style.color = "red";
        }
      }
      break;
    case 4: //On Thursday coloring is on sale
      if (
        hour >= locationOpeningHours.weekdayOpen &&
        locationOpeningHours.wednesdayClose > hour
      ) {
        for (const element of coloring) {
          element.style.textDecoration = "line-through";
        }
        for (const element of saleColoring) {
          element.innerText = `${todayText} 500 kr `;
          element.style.color = "red";
        }
      }
      break;
  }
}

//show the different flags for each lang
function showFlags() {
  document.getElementById("activeMenu").style.display = "none";

  const languages = document.getElementsByClassName("inActiveMenu");

  //Show the langs that the user can select
  for (const element of languages) {
    element.style.display = "block";
  }
}
