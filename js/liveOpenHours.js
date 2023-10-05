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
        monday: { open: 10, close: 16 },
        tuesday: { open: 10, close: 16 },
        wednesday: { open: 10, close: 16 },
        thursday: { open: 10, close: 16 },
        friday: { open: 10, close: 16 },
        saturday: { open: 12, close: 15 },
    },
    lulea: {
        monday: { open: 10, close: 17 },
        tuesday: { open: 10, close: 16 },
        wednesday: { open: 10, close: 15 },
        thursday: { open: 10, close: 16 },
        friday: { open: 10, close: 16 },
        saturday: { open: 12, close: 15 },
    },
};

const local = window.location.pathname.includes("lulea")
    ? openHours.lulea
    : window.location.pathname.includes("kiruna")
        ? openHours.kiruna
        : console.log("location does not exist");

console.log(local)

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
    } else {
        displayOpeningStatus(false);
    }
}

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

window.addEventListener("load", function () {
    setOpeningStatus(new Date());
});

