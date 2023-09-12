document.addEventListener("DOMContentLoaded", function () {
  var hasjs = document.getElementsByClassName("hasjs");

  // Loop through each element with the class "hasjs"
  for (var i = 0; i < hasjs.length; i++) {
    hasjs[i].style.display = "block";
  }
});

function dailySales(date) {
  let dailyD = document.getElementById("dailyDisc");
  let weekday = date.getDay();
  const longHair = document.getElementsByClassName("longHair");
  const saleLongHair = document.getElementsByClassName("saleLongHair");
  const shortHair = document.getElementsByClassName("shortHair");
  const saleShortHair = document.getElementsByClassName("saleShortHair");
  const beard = document.getElementsByClassName("beard");
  const saleBeard = document.getElementsByClassName("saleBeard");
  const coloring = document.getElementsByClassName("coloring");
  const saleColoring = document.getElementsByClassName("saleColoring");

  switch (weekday) {
    case 1:
      for (const element of longHair) {
        console.log(element.innerText);

        element.style.textDecoration = "line-through";
      }
      for (const element of saleLongHair) {
        element.innerText = "540 kr" + " ".repeat(5);
        element.style.color = "red";
      }
      break;
    case 2:
      for (const element of shortHair) {
        console.log(element.innerText);

        element.style.textDecoration = "line-through";
      }
      for (const element of saleShortHair) {
        element.innerText = "180 kr" + " ".repeat(5);
        element.style.color = "red";
      }
      break;
    case 3:
      for (const element of beard) {
        console.log(element.innerText);

        element.style.textDecoration = "line-through";
      }
      for (const element of saleBeard) {
        element.innerText = "135 kr" + " ".repeat(5);
        element.style.color = "red";
      }
      break;
    case 4:
      for (const element of coloring) {
        console.log(element.innerText);

        element.style.textDecoration = "line-through";
      }
      for (const element of saleColoring) {
        element.innerText = "504 kr" + " ".repeat(5);
        element.style.color = "red";
      }
      break;
  }
}
