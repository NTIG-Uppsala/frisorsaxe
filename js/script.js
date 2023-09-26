// If javscript is on all elements with hasjs class will show. They are by default not displayed.
document.addEventListener("DOMContentLoaded", function () {
  let hasjs = document.getElementsByClassName("hasjs");

  for (let i = 0; i < hasjs.length; i++) {
    hasjs[i].style.display = "block"; // Block shows element
  }
});

var navBarOpen = false; // Collapses the dropdown menu on the navbar in the mobile-port

function navBarToggled() {
  navBarOpen = !navBarOpen; // If called it will switch the variable, if true to false and if false to true
}

var prevScrollPosition = window.scrollY;

// Hides the navbar when scrolling down, shows when scrolling up.
window.onscroll = function () {
  // Will not hide navbar if its active on smaller screen
  if (navBarOpen === false) {
    let currentScrollPosition = window.scrollY;
    if (currentScrollPosition === 0) {
      // If the user at the top of the website show navbar
      document.getElementById("navbar").style.top = "0";
    } else if (prevScrollPosition > currentScrollPosition) {
      // Show navbar if user is scrolling up
      document.getElementById("navbar").style.top = "0";
    } else {
      document.getElementById("navbar").style.top = "-35vh"; // Hide navbar if user is scrolling down
    }
    // Update the previous scroll position
    prevScrollPosition = currentScrollPosition;
  }
};

//Save the current used language in localstorage to be used later.
document.addEventListener("DOMContentLoaded", function () {
  const Currentlanguage = document.getElementById("activeLang").alt;
  if (Currentlanguage === "svenskaflaggan") {
    localStorage.setItem("language", "swe");
  } else if (Currentlanguage === "englishflag") {
    localStorage.setItem("language", "eng");
  }
});

function dailySales(date) {
  const openHours = {
    kiruna: {
      mondayClose: 16,
      tuesdayClose: 16,
      wednesdayClose: 16,
      thursdayClose: 16,
    },
    lulea: {
      mondayClose: 17,
      tuesdayClose: 16,
      wednesdayClose: 15,
      thursdayClose: 16,
    },
  };

  // Checks if website is in Luleå or Kiruna and then changes the opening hours accordingly
  const locationOpeningHours = window.location.pathname.includes("lulea")
    ? openHours.lulea
    : window.location.pathname.includes("kiruna")
    ? openHours.kiruna
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

  //Hide all elements so the tests can work
  saleColoring.style.display = "none";
  saleBeard.style.display = "none";
  saleLongHair.style.display = "none";
  saleShorthair.style.display = "none";

  // Checks what day of the week it is and sets sales for that day
  switch (weekday) {
    case 1: // On Monday longhair is on sale
      if (
        //Before the store closes the sale will show
        hour < locationOpeningHours.mondayClose
      ) {
        saleLongHair.style.display = "block";
        longHair.style.textDecoration = "line-through";
      }
      break;
    case 2: // On Tuesday shorthair is on sale
      if (
        //Before the store closes the sale will show
        hour < locationOpeningHours.tuesdayClose
      ) {
        saleShorthair.style.display = "block";
        shortHair.style.textDecoration = "line-through";
      }
      break;
    case 3: // On Wednesday beard is on sale
      if (
        //Before the store closes the sale will show
        hour < locationOpeningHours.wednesdayClose
      ) {
        saleBeard.style.display = "block";
        beard.style.textDecoration = "line-through";
      }
      break;
    case 4: // On Thursday coloring is on sale
      if (
        //Before the store closes the sale will show
        hour < locationOpeningHours.thursdayClose
      ) {
        saleColoring.style.display = "block";
        coloring.style.textDecoration = "line-through";
        break;
      }
  }
}

// Show the different flags for each language
function showFlags() {
  document.getElementById("activeMenu").style.display = "none";

  const languages = document.getElementsByClassName("inActiveMenu");

  // Show the languages that the user can select
  for (const element of languages) {
    element.style.display = "block";
  }
}

// Moves the table for prices when the window is smaller than 767px to haircut section
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

// List of accepted zip codes
zipCodeListKiruna = [
  "98132",
  "98135",
  "98136",
  "98137",
  "98138",
  "98139",
  "98140",
  "98142",
  "98143",
  "98144",
  "98146",
  "98147",
];
zipCodeListLulea = ["96190", "96191", "96193", "96194"];

document.addEventListener("DOMContentLoaded", (event) => {
  document
    .querySelector("#zipCodeCheck form")
    .addEventListener("submit", (event) => {
      event.preventDefault(); // Prevents the site from reloading
      document.getElementById("outputAcceptedZipCode").style.display = "none";
      document.getElementById("outputNotValidZipCode").style.display = "none";
      document.getElementById("outputNonAcceptedZipCode").style.display =
        "none";

      let zipInput =
        event.submitter.parentNode.querySelector("#zipNumber").value;
      zipInput = zipInput.split(" ").join(""); //removes spaces from string

      if (zipInput.match(/\D/) != null) {
        // If there are no numbers
        document.getElementById("outputNotValidZipCode").style.display =
          "block";
      } else if (zipInput.length != 5) {
        // If the input isnt 5 numbers
        document.getElementById("outputNotValidZipCode").style.display =
          "block";
      } else if (
        zipCodeListKiruna.includes(zipInput) &&
        window.location.pathname.includes("kiruna")
      ) {
        // If the zip code is valid in kiruna
        document.getElementById("outputAcceptedZipCode").style.display =
          "block";
      } else if (
        zipCodeListLulea.includes(zipInput) &&
        window.location.pathname.includes("lulea")
      ) {
        // If the zip code is valid in lulea
        document.getElementById("outputAcceptedZipCode").style.display =
          "block";
      } else {
        // If zipcode is valid but out of range for house appointment
        document.getElementById("outputNonAcceptedZipCode").style.display =
          "block";
      }
    });
});