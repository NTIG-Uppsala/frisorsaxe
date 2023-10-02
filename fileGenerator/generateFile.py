import json

selectedLanguage = ["eng", "swe", "fin"]  # Change this to the desired language
selectedLocation = ["lulea", "kiruna"]  # Change this to the desired location

# Load the JSON translation file
translations = json.load(open("fileGenerator/translations.json"))


# Function to replace placeholders in the HTML template
def replacePlaceholders(htmlTemplate, language, location):
    # Get the translation for the selected language and location
    translation = translations.get(language, {}).get(location, {})

    # Replace placeholders in the HTML template with values from OPENDAYS
    if "OPENDAYS" in translation:
        opendays = "\n".join(
            [f"<p>{value}</p>" for value in translation["OPENDAYS"].values()]
        )
        htmlTemplate = htmlTemplate.replace("*OPENDAYS*", opendays)

    # Replace placeholders in the HTML template with values from OPENDAYSTIME
    if "OPENDAYSTIME" in translation:
        openDaysTime = "\n".join(
            [f"<p>{value}</p>" for value in translation["OPENDAYSTIME"].values()]
        )
        htmlTemplate = htmlTemplate.replace("*OPENDAYSTIME*", openDaysTime)

    # Replace placeholders in the HTML template
    for key, value in translation.items():
        placeholder = f"*{key}*"
        htmlTemplate = htmlTemplate.replace(
            placeholder, str(value)
        )  # Ensure the value is converted to a string

    return htmlTemplate


for language in selectedLanguage:
    for location in selectedLocation:
        htmlTemplate = open("fileGenerator/template.html", "r").read()
        translatedHtml = replacePlaceholders(htmlTemplate, language, location)

        # Define the file name for the translated HTML
        translatedFileName = location + language + ".html"

        # Create the translated HTML file and write the content
        with open(translatedFileName, "w") as translatedFile:
            translatedFile.write(translatedHtml)

        print(f"Translated HTML saved to '{translatedFileName}'")
