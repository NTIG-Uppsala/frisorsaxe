function goToSite(place) {
  const language = localStorage.getItem("language");
  window.location.href = `${place}${language}.html`;
}
