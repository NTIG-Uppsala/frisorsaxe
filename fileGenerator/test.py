import json

# Load the JSON translation file
translations = json.load(open("fileGenerator/translations.json"))


# Function to replace placeholders in the HTML template
def replace_placeholders(html_template, language, location):
    # Get the translation for the selected language and location
    translation = translations.get(language, {}).get(location, {})

    # Replace placeholders in the HTML template with values from OPENDAYS
    if "OPENDAYS" in translation:
        opendays = "\n".join(
            [f"<p>{value}</p>" for value in translation["OPENDAYS"].values()]
        )
        html_template = html_template.replace("*OPENDAYS*", opendays)

    # Replace placeholders in the HTML template with values from OPENDAYSTIME
    if "OPENDAYSTIME" in translation:
        opendaystime = "\n".join(
            [f"<p>{value}</p>" for value in translation["OPENDAYSTIME"].values()]
        )
        html_template = html_template.replace("*OPENDAYSTIME*", opendaystime)

    # Replace placeholders in the HTML template
    for key, value in translation.items():
        placeholder = f"*{key.upper()}*"
        html_template = html_template.replace(
            placeholder, str(value)
        )  # Ensure the value is converted to a string

    return html_template


# Example usage
selected_language = ["eng", "swe", "fin"]  # Change this to the desired language
selected_location = ["lulea", "kiruna"]  # Change this to the desired location
for language in selected_language:
    for location in selected_location:
        html_template = open("fileGenerator/template.html", "r").read()
        translated_html = replace_placeholders(html_template, language, location)

        # Define the file name for the translated HTML
        translated_file_name = location + language + ".html"

        # Create the translated HTML file and write the content
        with open(translated_file_name, "w") as translated_file:
            translated_file.write(translated_html)

        print(f"Translated HTML saved to '{translated_file_name}'")
