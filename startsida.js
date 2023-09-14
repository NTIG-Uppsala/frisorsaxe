function changeFlag() {
    const lang = document.getElementById("language").lang;
    const en = document.getElementsByClassName("enMenu");
    const sv = document.getElementsByClassName("svMenu");

    if (lang === "en") {
        console.log("en");
    } else if (lang === "sv") {
        console.log("sv");
    }
}
