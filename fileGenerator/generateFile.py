import json

# Load the JSON translation file
data = json.load(open("fileGenerator/data.json"))

common = data["COMMON"]
locations = data["LOCATIONS"]
langs = data["LANGS"]


# Function to replace placeholders in the HTML template
def replacePlaceholders(htmlTemplate, language, location):
    # Get the translation for the selected language and location
    locationInfo = locations[location]
    langsInfo = langs[language]

    # Replace placeholders in the HTML template with values from OPENDAYS
    # For every value in OPENDAYS, it creates a new <p> tag with the corresponding value on a new line.
    if "OPENDAYS" in langsInfo[location]:
        opendays = "\n".join(
            [f"<p>{value}</p>" for value in langsInfo[location]["OPENDAYS"].values()]
        )
        htmlTemplate = htmlTemplate.replace("*OPENDAYS*", opendays)

    # Replace placeholders in the HTML template with values from OPENDAYSTIME
    if "OPENDAYSTIME" in locationInfo:
        openDaysTime = "\n".join(
            [f"<p>{value}</p>" for value in locationInfo["OPENDAYSTIME"].values()]
        )
        htmlTemplate = htmlTemplate.replace("*OPENDAYSTIME*", openDaysTime)

    employee = 1  # The current employee number
    for employeeWork in langsInfo[location]["EMPLOYEESWORK"].values():
        # Replace placeholders in the HTML template with values from EMPLOYEESWORK
        htmlTemplate = htmlTemplate.replace(f"*PERS{employee}JOB*", employeeWork)
        employee += 1

    getMainAltText = langsInfo.get("FLAGALT", "Unknown language")

    htmlTemplate = htmlTemplate.replace("*MAINFLAG*", language + "Flag")

    htmlTemplate = htmlTemplate.replace("*MAINLANGFLAGALT*", getMainAltText)

    # Replace placeholders in the HTML template
    for key, value in common.items():
        placeholder = f"*{key}*"
        htmlTemplate = htmlTemplate.replace(
            placeholder, str(value)
        )  # Ensure the value is converted to a string
    for key, value in langsInfo.items():
        placeholder = f"*{key}*"
        htmlTemplate = htmlTemplate.replace(
            placeholder, str(value)
        )  # Ensure the value is converted to a string
    for key, value in locationInfo.items():
        placeholder = f"*{key}*"
        htmlTemplate = htmlTemplate.replace(
            placeholder, str(value)
        )  # Ensure the value is converted to a string
    return htmlTemplate


for language in langs:
    for location in locations:
        htmlTemplate = open("fileGenerator/template.html", "r").read()
        translatedHtml = replacePlaceholders(htmlTemplate, language, location)

        # Define the file name for the translated HTML
        translatedFileName = location.lower() + language + ".html"

        # Create the translated HTML file and write the content
        with open(translatedFileName, "w") as translatedFile:
            translatedFile.write(translatedHtml)

        print(f"Translated HTML saved to '{translatedFileName}'")
