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

## Adding a language for Frisör Saxé

1. **Edit the translations.json file:**

   - Open the translations.json file.
   - Locate the "swe" object within the JSON structure.
   - Copy the entire "swe" object, including all its keys and values.
   - Paste the copied object right after the last object in the list (make sure to maintain proper JSON formatting with commas).
   - The JSON object name should be the new language created, like “fre” for French.

2. **Translate the Values:**

   - Within the newly created object for the new language, change the values for each key so that they match the desired translations for that language.

3. **Update generateFile.py:**

   - Open the generateFile.py script.
   - Locate the selectedLanguage array in the script.
   - Add the language code (the same name used for the JSON object) to the selectedLanguage array as a string. Do not remove previous languages or locations in the array.

4. **Add the Flag Image:**

   - Place the picture of the country's flag in the "pictures" folder. Ensure that the image has the following properties:

     - Resolution: 640x373 pixels
     - Format: PNG

   - In the existing JSON objects except for the newly created one, locate the "THIRDVERSIONALT" field and confirm that "THIRD" is indeed the latest version.

   - If "Third" is the latest version, proceed to add the following fields: "FOURTHVERSIONALT," "FOURTHVERSIONSITE," and "FOURTHFLAG" to all JSON objects except the one you just created.

   - In the "FOURTHFLAG" field, ensure that the alt attribute contains "englishflag" translated into the respective language, for example, "svenskaflaggan."

   - Finally, incorporate this code into the list (ul tag) identified by the id "flagMenu" in the template, replace "FOURTHFLAG" if necessary.

&#x20;

    <li>
        <a class="inActiveMenu flag" href="*FOURTHVERSIONSITE*">
            <img src="pictures/*FOURTHFLAG*.png" alt="*FOURTHVERSIONALT*">
        </a>
    </li>

5. **Change main language**

   - In the JSON object you created, locate all the keys that start with MAIN and change their value so they fit the newly created language.
   - The appearance of the flag does not affect the code. However make sure that all the languages have their own version, with alt and html file in all JSON objects.

6. **Add language to localstorage**

   - Open script.js and located the variable Currentlanguage.
   - Add another else if statement like the ones created before.
   - Make sure the new else if statement is looking for the newly created alt for the new flag.

7. **Run generateFile.py:**

   - Execute the generateFile.py script.
   - Check how the newly added language appears on the generated HTML page.

**Note: Please ensure that you maintain the proper JSON structure and formatting when editing the translations.json file.**

**Occasionally, adjustments may be necessary, depending on the linguistic structure, especially when dealing with languages outside the Latin alphabet, which have not undergone extensive testing.**

---
