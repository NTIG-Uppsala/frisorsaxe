import json
import os
import shutil

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the available languages and their corresponding locations
languages_and_locations = {
    "swe": {"lulea": "lulea"}
    # "eng": {"lulea": "lulea", "kiruna": "kiruna"},
}

# Load the JSON data from the file
with open(
    os.path.join(script_directory, "translations.json"), "r", encoding="utf-8"
) as json_file:
    translations = json.load(json_file)

# Loop through languages and locations
for language, locations in languages_and_locations.items():
    for location_code, location_name in locations.items():
        # Check if the language exists in the JSON data
        if language not in translations:
            print(f"Language '{language}' not found in translations.")
        elif location_code not in translations[language]:
            print(
                f"Location '{location_code}' not found in translations for '{language}'."
            )
        else:
            # Duplicate the HTML template file
            template_file = os.path.join(script_directory, "template.html")
            output_file_path = os.path.join(
                script_directory, f"{language}_{location_code}.html"
            )
            shutil.copy(template_file, output_file_path)

            # Read the duplicated HTML file
            with open(output_file_path, "r", encoding="utf-8") as html_file:
                html_content = html_file.read()

            # Replace the first word in the HTML content with its translation
            first_word = html_content.split()[0]  # Get the first word
            translation = translations[language][location_code].get(
                first_word, first_word
            )
            html_content = html_content.replace(first_word, translation)

            # Write the modified HTML content back to the file
            with open(output_file_path, "w", encoding="utf-8") as output_file:
                output_file.write(html_content)

            print(f"{language}_{location_code}.html file has been generated.")
