import re

from translate import Translator

# Specify the path to your HTML file
html_file_path = "index.html"

# Read the HTML content from the file
try:
    with open(html_file_path, "r", encoding="utf-8") as html_file:
        html_content = html_file.read()
except FileNotFoundError:
    print(f"File '{html_file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Create a dictionary to store translation pairs (English to Swedish)
translation_dict = {}

# Read the translation pairs from a text file
translation_file_path = "translation.txt"

try:
    with open(translation_file_path, "r", encoding="utf-8") as translation_file:
        for line in translation_file:
            line = line.strip()
            if "=" in line:
                english, swedish = line.split("=")
                translation_dict[english.strip()] = swedish.strip()
except FileNotFoundError:
    print(f"Translation file '{translation_file_path}' not found.")
except Exception as e:
    print(f"An error occurred while reading the translation file: {str(e)}")

# Define a regular expression pattern to find text between single asterisks
pattern = r"\*([^*]+)\*"


# Function to translate text
def translate_text(text, target_language):
    try:
        if text in translation_dict:
            return translation_dict[text]
        else:
            translator = Translator(to_lang=target_language)
            translation = translator.translate(text)
            return translation
    except Exception as e:
        print(f"Translation error: {str(e)}")
        return text  # Return the original text if translation fails


# Set the target language variable (either "sv" for Swedish or "en" for English)
swedish_target_language = "sv"
english_target_language = "en"

# Translate and replace the matches in the HTML content for Swedish
swedish_html_content = html_content
for match in re.findall(pattern, html_content):
    translated_text = translate_text(match, swedish_target_language)
    swedish_html_content = swedish_html_content.replace(f"*{match}*", translated_text)

# Translate and replace the matches in the HTML content for English
english_html_content = html_content
for match in re.findall(pattern, html_content):
    translated_text = translate_text(match, english_target_language)
    english_html_content = english_html_content.replace(f"*{match}*", translated_text)

# Save the translated HTML content to separate files
with open("index_sv.html", "w", encoding="utf-8") as swedish_file:
    swedish_file.write(swedish_html_content)

with open("index_en.html", "w", encoding="utf-8") as english_file:
    english_file.write(english_html_content)

print("Translation completed and saved to 'index_sv.html' and 'index_en.html'.")
