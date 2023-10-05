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
        displayOpeningStatus(false);
        return;
    }

    // Use the specified location's opening hours
    const locationHours = local[weekday];

    if (hour >= locationHours.open && hour < locationHours.close) {
        displayOpeningStatus(true);
    } else if (hour < locationHours.open) {
        displayOpeningStatus("day", locationHours.open);
    } else {
        // Check if it's Saturday (6) and adjust for Sunday (0) or continue to the next day
        const nextDayIndex = (day === 6) ? 0 : (day + 1);
        displayOpeningStatus("tom", local[days[nextDayIndex]].open);
    }
}

// Define global variables to store the original content
let originalClosedContent;
let originalOpenContent;
let originalOpenTomContent;
let originalOpenToDayContent;

// Displays the opening status on the page
function displayOpeningStatus(status, time) {
    const closedElement = document.getElementById("displayedIfClosed");
    const openElement = document.getElementById("displayedIfOpen");
    const openTomElement = document.getElementById("displayedIfOpenTom");
    const openToDayElement = document.getElementById("displayedIfOpenToDay");

    if (originalClosedContent === undefined) {
        // Store the original content on the first function call
        originalClosedContent = closedElement.innerHTML;
        originalOpenContent = openElement.innerHTML;
        originalOpenTomContent = openTomElement.innerHTML;
        originalOpenToDayContent = openToDayElement.innerHTML;
    }

    if (status === true) {
        openElement.style.display = "block";
        closedElement.style.display = "none";
        openToDayElement.style.display = "none";
    } else {
        closedElement.style.display = "block";
        openElement.style.display = "none";
        if (status === "day") {
            openTomElement.style.display = "none";
            openToDayElement.style.display = "block";
            openToDayElement.innerHTML = originalOpenToDayContent + " " + time;
        } else {
            openTomElement.style.display = "block";
            openToDayElement.style.display = "none";
            openTomElement.innerHTML = originalOpenTomContent + " " + time;
        }
    }
}

window.addEventListener("load", function () {
    setOpeningStatus(new Date());
});

