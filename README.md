# Frisör Saxé

Repository for Frisör Saxé worked on 2023-2024.

[Link to live server](https://ntig-uppsala.github.io/frisorsaxe/)

## Coding standard

- All variables are in English, start with lowercase letters and subsequent words start with uppercase letters (camelCase). Eventual snake_case is from/for bootstrap.
- We use four blank spaces for indentation.
- All test functions have to start with "test".
- English file names only contain lowercase letters. Except for pictures, which have no standard.
- Comments are positioned above the or next to the code depending on how the formatter formats it, are only in English and start with Uppercase.
- Python files follow the Black Formatter standard and Pylint with the exception of C0111 and method-naming-style=camelCase.

## Testing

Our website uses the software Selenium and Python's unittest library to run tests.

## Development environment

- Code Editor: Visual Studio Code Version 1.82.2
- Google Chrome is the browser we use for testing.
- We use Windows 10 as our operating system.

## Programming languages

- HTML5 for creating websites
- CSS3 and Bootstrap 5.2.1 for styling
- Javascript ECMAScript 2023
- Python 3.11.5 and Selenium 4.11.2 for testing

## License
-  All images should be linked under the "licences" folder in "licenseLinks".
- Licenses for google fonts exist in the "licenses" folder located in the root folder.
- All of the photos are from either Unsplash and Pexels. Both of these websites exclusively have open licenses. (As long as you use the free version which we do.)

## Documentation

### Adding a language for Frisör Saxé

1. **Edit the data.json file:**

   - Open the "data.json" file located in the fileGenerator folder.
   - Locate the "sv" object within the JSON structure.
   - Copy the entire "sv" object, including all its keys and values.
   - Paste the copied object right after the last object in the list (make sure to maintain proper JSON formatting with commas).
   - The JSON object name should be the new language created in HTML standard format, like “fr” for French.

2. **Translate the Values:**

   - Within the newly created object for the new language, change the values for each key so that they match the desired translations for that language.

3. **Add the Flag Image:**

   - Place the picture of the country's flag in the "pictures" folder. Ensure that the image has the following properties:
     - Flagname should be named after HTML-lang-standard + "Flag". ex "frFlag" for French.
     - Resolution: 150x87 pixels 
     - Format: PNG

4. **Run generateFile.py:**

   - Execute the generateFile.py script located fileGenerator folder.
   - Check how the newly added language appears on the generated HTML page.

**Note: Please ensure that you maintain the proper JSON structure and formatting when editing the data.json file.**

**Occasionally, adjustments may be necessary, depending on the linguistic structure, especially when dealing with languages outside the Latin alphabet, which have not undergone extensive testing.**

---
