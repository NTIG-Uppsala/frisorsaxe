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
      document.getElementById("navbar").style.top = "-35vh";
    }
    // Update the previous scroll position
    prevScrollPosition = currentScrollPosition;
  }
};

function dailySales(date) {
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
    ? openHours.lulea //In Luleas website
    : window.location.pathname.includes("kiruna")
      ? openHours.kiruna //In Kirunas website
      : console.log("location does not have openingHours for dailysailes");

  const weekday = date.getDay();
  const hour = date.getHours();

  const saleLongHair = document.getElementById("saleLongHair");
  const longHair = document.getElementById("longHair");

  const saleShorthair = document.getElementById("saleShortHair");
  const shortHair = document.getElementById("shortHair");

  const saleBeard = document.getElementById("saleBeard");
  const beard = document.getElementById("beard");

  const saleColoring = document.getElementById("saleColoring");
  const coloring = document.getElementById("coloring");

  switch (weekday) {
    case 1: //On Monday longhair is on sale
      if (
        //If we are open
        hour >= locationOpeningHours.weekdayOpen &&
        locationOpeningHours.mondayClose > hour
      ) {
        saleLongHair.style.display = "block";
        longHair.style.textDecoration = "line-through";
      }
      break;
    case 2: //On Tuesday shorthair is on sale
      if (
        //If we are open
        hour >= locationOpeningHours.weekdayOpen &&
        locationOpeningHours.tuesdayClose > hour
      ) {
        saleShorthair.style.display = "block";
        shortHair.style.textDecoration = "line-through";
      }
      break;
    case 3: //On Wednesday beard is on sale
      if (
        //If we are open
        hour >= locationOpeningHours.weekdayOpen &&
        locationOpeningHours.tuesdayClose > hour
      ) {
        saleBeard.style.display = "block";
        beard.style.textDecoration = "line-through";
      }
      break;
    case 4: //On Thursday coloring is on sale
      if (
        //If we are open
        hour >= locationOpeningHours.weekdayOpen &&
        locationOpeningHours.tuesdayClose > hour
      ) {
        saleColoring.style.display = "block";
        coloring.style.textDecoration = "line-through";
        break;
      }
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

//Only breads the mail if the screen is smaller then 700px
function mailLineBreak() {
  const mail = document.getElementById("mailLink");
  if (window.location.pathname.includes("kiruna")) {
    if (window.innerWidth <= 700) {
      mail.innerHTML = "info@ntig-uppsala.github.io";
    } else {
      mail.innerHTML = "info@ntig&#8209;uppsala.github.io";
    }
  } else if (window.location.pathname.includes("lulea")) {
    if (window.innerWidth <= 700) {
      mail.innerHTML = "lulea@ntig-uppsala.github.io";
    } else {
      mail.innerHTML = "lulea@ntig&#8209;uppsala.github.io";
    }
  }
}

function regularCustomerInfo() {
  const regularInfo = document.getElementById("regularCustomerInfo");
  const regularInfoOther = document.getElementById("regularCustomerInfoOther");

  if (window.innerWidth <= 767) {
    regularInfo.style.display = "block";
    regularInfoOther.style.display = "none";
  } else {
    regularInfo.style.display = "none";
    regularInfoOther.style.display = "block";
  }
}

// Call the function when the page loads and when the window is resized
window.addEventListener("load", regularCustomerInfo);
window.addEventListener("resize", regularCustomerInfo);

window.onresize = mailLineBreak;

// List of accepted zip codes
zipCodeListKiruna = [
  "98132",
  "98135",
  "98136",
  "98138",
  "98137",
  "98139",
  "98140",
  "98142",
  "98143",
  "98144",
  "98146",
  "98147"
];
zipCodeListLulea = [
  "96193",
  "96194",
  "96190",
  "96191"

]

//  Runs when the document is fully loaded
document.addEventListener("DOMContentLoaded", (event) => {
  document
    .querySelector("#zipCodeCheck form")
    .addEventListener("submit", (event) => {
      event.preventDefault(); // Prevents the default action

      // event.submitter.parentNode.querySelector("#number").value
      // Is what is written in the input
      let zipInput =
        event.submitter.parentNode.querySelector("#zipNumber").value;
      zipInput = zipInput.split(" ").join(""); //removes spaces from string

      if (zipInput.match(/\D/) != null) {
        // If there are no numbers
        document.querySelector("#output").innerHTML =
          "Inte ett giltigt postnummer.";
      } else if (zipInput.length != 5) {
        // If there are more or less then 5 numbers
        document.querySelector("#output").innerHTML =
          "Inte ett giltigt postnummer.";
      } else if (zipCodeListKiruna.includes(zipInput) && window.location.pathname.includes("kiruna")) {
        // If the zip code is valid in kiruna
        document.querySelector("#output").innerHTML =
          "Vi kör ut, ring telefonnumret ovan!";
      } else if (zipCodeListLulea.includes(zipInput) && window.location.pathname.includes("lulea")) {
        // If the zip code is valid in lulea
        document.querySelector("#output").innerHTML =
          "Vi kör ut, ring telefonnumret ovan!";
      } else {
        // If the zip code is invalid
        document.querySelector("#output").innerHTML =
          "Vi kör tyvärr inte ut till dig.";
      }
    });
});
