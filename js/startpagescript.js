function goToSite(place) {
  const language = localStorage.getItem("language") || "swe";
  window.location.href = `subpages/${place}${language}.html`;
}

function arrowShow() {
  const arrow = document.getElementById("arrowForPhonesDown");
  if (window.scrollY > 650) {
    arrow.style.opacity = 0;
  } else {
    arrow.style.opacity = 1;
  }
}
