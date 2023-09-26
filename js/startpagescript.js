function goToSite(place) {
  const language = localStorage.getItem("language") || "swe";
  window.location.href = `subpages/${place}${language}.html`;
}

function arrowShow() {
  let limit = Math.max(
    document.body.scrollHeight,
    document.body.offsetHeight,
    document.documentElement.clientHeight,
    document.documentElement.scrollHeight,
    document.documentElement.offsetHeight
  );
  const arrowDown = document.getElementById("arrowForPhonesDown");
  const arrowUp = document.getElementById("arrowForPhonesUp");
  console.log(limit - window.innerHeight);
  console.log(window.scrollY);

  if (limit - window.innerHeight - window.scrollY < 50) {
    arrowDown.style.opacity = 0;
    arrowUp.style.opacity = 1;
  } else {
    arrowDown.style.opacity = 1;
    arrowUp.style.opacity = 0;
  }
}
