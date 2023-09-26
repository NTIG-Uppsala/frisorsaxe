function goToSite(place) {
  // Navigate to the previously selected language, or default to Swedish if none is available.
  const language = localStorage.getItem("language") || "swe";
  window.location.href = `${place}${language}.html`;
}
function arrowShow() {
  // Calculate the maximum height of the webpage content
  let limit = Math.max(
    document.body.scrollHeight,
    document.body.offsetHeight,
    document.documentElement.clientHeight,
    document.documentElement.scrollHeight,
    document.documentElement.offsetHeight
  );

  // Get references to the arrow elements
  const arrowDown = document.getElementById("arrowForPhonesDown");
  const arrowUp = document.getElementById("arrowForPhonesUp");

  // (Limit - innerHeight) is how many pixels there is left to the bottom of the site.
  // If there is 150px left to bottom and you then scroll 100px down the arrowDown will show.
  if (limit - window.innerHeight - window.scrollY < 50) {
    arrowDown.style.display = "none"; // Hide
    arrowUp.style.display = "block"; // Show
  } else {
    arrowDown.style.display = "block";
    arrowUp.style.display = "none";
  }
}
