window.setInterval(function () {
    setOpeningStatus(new Date());
}, 5000); //Every 30 sec

const days = [
    "söndag",
    "måndag",
    "tisdag",
    "onsdag",
    "torsdag",
    "fredag",
    "lördag",
];

// Globally defines the opening hours array
const openingHoursKiruna = {
    monday: { open: 10, close: 16 },
    tuesday: { open: 10, close: 16 },
    wednesday: { open: 10, close: 16 },
    thursday: { open: 10, close: 16 },
    friday: { open: 10, close: 16 },
    saturday: { open: 12, close: 15 },
};
const openingHoursLulea = {
    monday: { open: 10, close: 17 },
    tuesday: { open: 10, close: 16 },
    wednesday: { open: 10, close: 15 },
    thursday: { open: 10, close: 16 },
    friday: { open: 10, close: 16 },
    saturday: { open: 12, close: 15 },
};

// Gets and changes the opening status
function setOpeningStatus(date) {
    const hour = date.getHours();
    const day = date.getDay();
    const weekday = days[day];

    console.log(weekday)

    // Sets the opening hours and checking for the special case of Saturday
    let openingTime = openingHoursKiruna.weekday.open

    console.log(openingTime)

    let closingTime = openingHoursKiruna.weekday.close

    console.log(closingTime)

    if (hour >= openingTime && hour < closingTime) {  // If the store is opened
        displayOpeningStatus(true);
    } else { // Has closed for the day
        displayOpeningStatus(false);
    };
};

// Displays the opening status on the page
function displayOpeningStatus(status) {
    const closedElement = document.getElementById("displayedIfClosed");
    const openElement = document.getElementById("displayedIfOpen");
    if (status) {
        openElement.style.display = "block";
        closedElement.style.display = "none";
    } else {
        closedElement.style.display = "block";
        openElement.style.display = "none";
    }
}