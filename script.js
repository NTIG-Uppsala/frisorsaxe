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
      dailyD = longHair;
      dailyD.innerText = "Idag är det 10% rea på klippning av långt hår.";
      break;
    case 2:
      for (const element of shortHair) {
        console.log(element.innerText);

        element.style.textDecoration = "line-through";
      }
      /*for (const element of saleShortHair) {
        element.innerText = "180 kr" + ' '.repeat(5);
        element.style.color = "red"

      }*/
      break;
    case 3:
      dailyD.innerText = "Idag är det 10% rea på barbering.";
      break;
    case 4:
      dailyD.innerText =
        "Idag är det 10% rea på färging av alla längder av hår.";
      break;
  }
}

function saleCalc() {}
