import json

# Load the JSON translation file
data = json.load(open("fileGenerator/data.json"))

common = data["COMMON"]
locations = data["LOCATIONS"]
langs = data["LANGS"]


# Function to replace placeholders in the HTML template
def replacePlaceholders(htmlTemplate, language, location):
    locationInfo = locations[location]
    langsInfo = langs[language]

    # Replace placeholders in the HTML template with values from OPENDAYS
    # For every value in OPENDAYS, it creates a new <p> tag with the corresponding value on a new line.
    openDays = "\n".join(
        [
            f"<p>{value}</p>"
            for value in langsInfo[location].get("OPENDAYS", {}).values()
        ]
    )
    htmlTemplate = htmlTemplate.replace("*OPENDAYS*", openDays)

    # Same principle as openDays.
    openDaysTime = "\n".join(
        [f"<p>{value}</p>" for value in locationInfo.get("OPENDAYSTIME", {}).values()]
    )
    htmlTemplate = htmlTemplate.replace("*OPENDAYSTIME*", openDaysTime)

    # Looks for Employeeswork object
    for i, employeeWork in enumerate(
        langsInfo[location]["EMPLOYEESWORK"].values(), start=1
    ):
        htmlTemplate = htmlTemplate.replace(f"*PERS{i}JOB*", employeeWork)

    mainFlagAlt = common["LANG"][language.upper() + "FLAGALT"]

    htmlTemplate.replace("*MAINLANGFLAGALT*", mainFlagAlt)
    htmlTemplate = htmlTemplate.replace("*MAINFLAG*", language + "Flag")

    flagList = []

    for languageUsed in langs.keys():
        # Get the alternative text for the flag image from the 'common' dictionary
        altText = common["LANG"].get(languageUsed.upper() + "FLAGALT")

        # Check if the current language matches the 'language' variable
        if languageUsed == language:
            # Insert the HTML list item with 'mainFlagAlt' at the beginning of 'flagList' to ensure it appears first in the flag menu on the website.
            flagList.insert(
                0,
                f'<li><a href="{location.lower() + language}.html" class="inActiveMenu flag"><img src="pictures/{language}Flag.png" alt="{altText}"></a></li>',
            )
        else:
            # Append the HTML list item to 'flagList'
            flagList.append(
                f'<li><a href="{location.lower() + languageUsed}.html" class="inActiveMenu flag"><img src="pictures/{languageUsed}Flag.png" alt="{altText}"></a></li>'
            )

    # Join the list of HTML list items into a single string, separated by newline characters
    flagList = "\n".join(flagList)

    htmlTemplate = htmlTemplate.replace("*FLAGLIST*", flagList)

    for key, value in common.items():
        htmlTemplate = htmlTemplate.replace(f"*{key}*", str(value))
    for key, value in langsInfo.items():
        htmlTemplate = htmlTemplate.replace(f"*{key}*", str(value))
    for key, value in locationInfo.items():
        htmlTemplate = htmlTemplate.replace(f"*{key}*", str(value))

    return htmlTemplate


for language in langs:
    for location in locations:
        htmlTemplate = open("fileGenerator/template.html", "r").read()
        translatedHtml = replacePlaceholders(htmlTemplate, language, location)
        translatedFileName = location.lower() + language + ".html"

        # Create the translated HTML file and write the content
        with open(translatedFileName, "w") as translatedFile:
            translatedFile.write(translatedHtml)

        print(f"Translated HTML saved to '{translatedFileName}'")
