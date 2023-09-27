import json
import shutil
import os

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the language name (e.g., "English" or "Swedish")
language_name = "Swedish"

# Construct the path to the JSON file in the same directory as the script
json_file_path = os.path.join(script_directory, "translations.json")

# Load the JSON data from the file
with open(json_file_path, "r", encoding="utf-8") as json_file:
    translations = json.load(json_file)

# Check if the chosen language exists in the JSON data
if language_name not in translations:
    print(f"Language '{language_name}' not found in translations.")
else:
    # Duplicate the HTML template file
    shutil.copy(
        os.path.join(script_directory, "template.html"), f"{language_name}.html"
    )

    # Read the duplicated HTML file
    with open(f"{language_name}.html", "r", encoding="utf-8") as html_file:
        html_content = html_file.read()

    # Replace placeholders in the HTML content with translations
    for word_translation_pair in translations[language_name]:
        word = word_translation_pair["word"]
        translation = word_translation_pair["translation"]
        html_content = html_content.replace(word, translation)

    # Write the modified HTML content back to the file
    with open(f"{language_name}.html", "w", encoding="utf-8") as output_file:
        output_file.write(html_content)

    print(f"{language_name} HTML file has been generated.")
