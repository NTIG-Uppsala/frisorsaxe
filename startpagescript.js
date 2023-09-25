function goToSite(place) {
  const language = localStorage.getItem("language") || "swe";
  window.location.href = `${place}${language}.html`;
}
