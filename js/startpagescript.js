function goToSite(place) {
  // Goes to last used language if there is any else Swedish site
  const language = localStorage.getItem("language") || "swe";
  window.location.href = `${place}${language}.html`;
}

function arrowShow() {
  let limit = Math.max(
    // Max height of site
    document.body.scrollHeight,
    document.body.offsetHeight,
    document.documentElement.clientHeight,
    document.documentElement.scrollHeight,
    document.documentElement.offsetHeight
  );
  const arrowDown = document.getElementById("arrowForPhonesDown");
  const arrowUp = document.getElementById("arrowForPhonesUp");

  // 50 pixels from the bottom of the screen
  if (limit - window.innerHeight - window.scrollY < 50) {
    // Shows arrow do go down
    arrowDown.style.display = "none";
    arrowUp.style.display = "block";
  } else {
    // Show arrow to go up
    arrowDown.style.display = "block";
    arrowUp.style.display = "none";
  }
}
