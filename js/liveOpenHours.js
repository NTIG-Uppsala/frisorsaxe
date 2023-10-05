window.setInterval(function () {
    setOpeningStatus(new Date());
}, 30000); // Every 30 seconds

const days = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
];

// Define opening hours for both locations
const openHours = {
    kiruna: {
        sunday: { open: 0, close: 0 },
        monday: { open: 10, close: 16 },
        tuesday: { open: 10, close: 16 },
        wednesday: { open: 10, close: 16 },
        thursday: { open: 10, close: 16 },
        friday: { open: 10, close: 16 },
        saturday: { open: 12, close: 15 },
    },
    lulea: {
        sunday: { open: 0, close: 0 },
        monday: { open: 10, close: 17 },
        tuesday: { open: 10, close: 16 },
        wednesday: { open: 10, close: 15 },
        thursday: { open: 10, close: 16 },
        friday: { open: 10, close: 16 },
        saturday: { open: 12, close: 15 },
    },
};
// Checks what location the user is in
const local = window.location.pathname.includes("lulea")
    ? openHours.lulea
    : window.location.pathname.includes("kiruna")
        ? openHours.kiruna
        : console.log("location does not exist");

// Gets and changes the opening status based on location and day
function setOpeningStatus(date) {
    const hour = date.getHours();
    const day = date.getDay();
    const weekday = days[day];

    if (weekday === "sunday") {
        displayOpeningStatus("tom", local.monday.open);
        return;
    }

    // Use the specified location's opening hours
    const locationHours = local[weekday];

    if (hour >= locationHours.open && hour < locationHours.close) {
        displayOpeningStatus(true);
    } else if (hour < locationHours.open) {
        displayOpeningStatus("day", locationHours.open);
    } else {
        if (weekday === "saturday") {
            displayOpeningStatus("saturday", local.monday.open);
            return;
        } else {
            displayOpeningStatus("tom", local[days[day + 1]].open);
        }
    }
}

// Define global variables to store the original content
let originalClosedContent;
let originalOpenContent;
let originalOpenTomContent;
let originalOpenToDayContent;
let originalOpenSaturdayContent;

// Displays the opening status on the page
function displayOpeningStatus(status, time) {
    const closedElement = document.getElementById("displayedIfClosed");
    const openElement = document.getElementById("displayedIfOpen");
    const openTomElement = document.getElementById("displayedIfOpenTom");
    const openToDayElement = document.getElementById("displayedIfOpenToDay");
    const openSaturdayElement = document.getElementById("displayedIfOpenMonday");

    if (originalClosedContent === undefined) {
        // Store the original content on the first function call
        originalClosedContent = closedElement.innerHTML;
        originalOpenContent = openElement.innerHTML;
        originalOpenTomContent = openTomElement.innerHTML;
        originalOpenToDayContent = openToDayElement.innerHTML;
        originalOpenSaturdayContent = openSaturdayElement.innerHTML;
    }

    if (status === true) {
        openElement.style.display = "block";
        closedElement.style.display = "none";
        openToDayElement.style.display = "none";
    } else {
        closedElement.style.display = "block";
        openElement.style.display = "none";
        if (status === "day") {
            openToDayElement.style.display = "block";
            openTomElement.style.display = "none";
            openSaturdayElement.style.display = "none";
            openToDayElement.innerHTML = originalOpenToDayContent + " " + time;
        } else if (status === "tom") {
            openTomElement.style.display = "block";
            openToDayElement.style.display = "none";
            openSaturdayElement.style.display = "none";
            openTomElement.innerHTML = originalOpenTomContent + " " + time;
        } else if (status === "saturday") {
            openSaturdayElement.style.display = "block";
            openToDayElement.style.display = "none";
            openTomElement.style.display = "none";
            openSaturdayElement.innerHTML = originalOpenSaturdayContent + " " + time;
        } else {
            console.log("something went wrong")
        }
    }
}

window.addEventListener("load", function () {
    setOpeningStatus(new Date());
});

