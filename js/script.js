// If javscript is on, all elements with hasjs class will show. They are by default not displayed.
document.addEventListener("DOMContentLoaded", function () {
  let hasjs = document.getElementsByClassName("hasjs");

  for (let i = 0; i < hasjs.length; i++) {
    hasjs[i].style.display = "block"; // Block shows element
  }
});

var navBarOpenMobile = false;

function navBarToggled() {
  navBarOpenMobile = !navBarOpenMobile; // If called it will switch the variable, if true to false and if false to true
  hideFlags();
}

var prevScrollPosition = window.scrollY;

// Hides the navbar when scrolling down, shows when scrolling up.
window.onscroll = function () {
  if (navBarOpenMobile === false) {
    let currentScrollPosition = window.scrollY; // Pixels that the document is currently scrolled vertically.
    if (currentScrollPosition === 0) {
      document.getElementById("navbar").style.top = "0";
    } else if (prevScrollPosition > currentScrollPosition) {
      // Show navbar if user is scrolling up
      document.getElementById("navbar").style.top = "0";
    } else {
      document.getElementById("navbar").style.top = "-35vh"; // Hide navbar if user is scrolling down
      hideFlags();
    }
    // Update the previous scroll position
    prevScrollPosition = currentScrollPosition;
  }
};

function hideFlags() {
  document.getElementById("activeMenu").style.display = "block";

  const languages = document.getElementsByClassName("inActiveMenu");

  // Show the languages that the user can select
  for (const element of languages) {
    element.style.display = "none";
  }
}

//Save the current used language in localstorage to be used later.
document.addEventListener("DOMContentLoaded", function () {
  const Currentlanguage = document.getElementById("activeLang").alt;
  if (Currentlanguage === "svenskaflaggan") {
    localStorage.setItem("language", "swe");
  } else if (Currentlanguage === "englishflag") {
    localStorage.setItem("language", "eng");
  } else if (Currentlanguage === "suomenlippu") {
    localStorage.setItem("language", "fin");
  }
});

function dailySales(date) {
  const openHours = {
    kiruna: {
      mondayCloseHour: 16,
      tuesdayCloseHour: 16,
      wednesdayCloseHour: 16,
      thursdayCloseHour: 16,
    },
    lulea: {
      mondayCloseHour: 17,
      tuesdayCloseHour: 16,
      wednesdayCloseHour: 15,
      thursdayCloseHour: 16,
    },
  };

  // Checks if website is in Luleå or Kiruna and then changes the opening hours accordingly
  const locationOpeningHours = window.location.pathname.includes("lulea")
    ? openHours.lulea
    : window.location.pathname.includes("kiruna")
    ? openHours.kiruna
    : console.log("location does not have openingHours for dailysailes");

  const weekday = date.getDay();
  const currentHour = date.getHours();

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

  switch (weekday) {
    case 1: // On Monday longhair is on sale
      if (currentHour < locationOpeningHours.mondayCloseHour) {
        saleLongHair.style.display = "block";
        longHair.style.textDecoration = "line-through";
      }
      break;
    case 2: // On Tuesday shorthair is on sale
      if (currentHour < locationOpeningHours.tuesdayCloseHour) {
        saleShorthair.style.display = "block";
        shortHair.style.textDecoration = "line-through";
      }
      break;
    case 3: // On Wednesday beard is on sale
      if (currentHour < locationOpeningHours.wednesdayCloseHour) {
        saleBeard.style.display = "block";
        beard.style.textDecoration = "line-through";
      }
      break;
    case 4: // On Thursday coloring is on sale
      if (currentHour < locationOpeningHours.thursdayCloseHour) {
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
  const infoOnPhone = document.getElementById("infoOnPhone");
  const infoOnDesktop = document.getElementById("infoOnDesktop");

  if (window.innerWidth <= 767) {
    infoOnPhone.style.display = "block";
    infoOnDesktop.style.display = "none";
  } else {
    infoOnPhone.style.display = "none";
    infoOnDesktop.style.display = "block";
  }
}

// Call the function when the page loads and when the window is resized
window.addEventListener("load", regularCustomerInfo);
window.addEventListener("resize", regularCustomerInfo);

// List of accepted postal codes
postalCodeListKiruna = [
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
postalCodeListLulea = ["96190", "96191", "96193", "96194"];

document.addEventListener("DOMContentLoaded", (event) => {
  document
    .querySelector("#postalCodeCheck form")
    .addEventListener("submit", (event) => {
      event.preventDefault(); // Prevents the site from reloading
      document.getElementById("outputAcceptedPostalCode").style.display =
        "none";
      document.getElementById("outputNotValidPostalCode").style.display =
        "none";
      document.getElementById("outputNonAcceptedPostalCode").style.display =
        "none";

      let postalInput =
        event.submitter.parentNode.querySelector("#postalCodeNumber").value;
      postalInput = postalInput.split(" ").join(""); //removes spaces from string

      if (postalInput.match(/\D/) != null) {
        // If there are no numbers
        document.getElementById("outputNotValidPostalCode").style.display =
          "block";
      } else if (postalInput.length != 5) {
        // If the input isnt 5 numbers
        document.getElementById("outputNotValidPostalCode").style.display =
          "block";
      } else if (
        postalCodeListKiruna.includes(postalInput) &&
        window.location.pathname.includes("kiruna")
      ) {
        // If the postal code is valid in kiruna
        document.getElementById("outputAcceptedPostalCode").style.display =
          "block";
      } else if (
        postalCodeListLulea.includes(postalInput) &&
        window.location.pathname.includes("lulea")
      ) {
        // If the postal code is valid in lulea
        document.getElementById("outputAcceptedPostalCode").style.display =
          "block";
      } else {
        // If PostalCode is valid but out of range for house appointment
        document.getElementById("outputNonAcceptedPostalCode").style.display =
          "block";
      }
    });
});
