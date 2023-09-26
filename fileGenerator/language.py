fileNames = ["kuirnakurish"]

# Step 1: Read and parse the HTML file
with open("fileGenerator/template.html", "r", encoding="utf-8") as html_file:
    html_content = html_file.read()

# Step 2: Read the text document with variable replacements
for fileName in fileNames:
    with open(
        "fileGenerator/" + fileName + ".txt", "r", encoding="utf-8"
    ) as variables_file:
        variables = {}
        for line in variables_file:
            key, value = line.strip().split("|")
            variables[key] = value

    # Step 3: Replace variables in the HTML content
    for variable, value in variables.items():
        html_content = html_content.replace(f"^{variable}^", value)
        html_content = html_content.replace(f"*{variable}*", value)

    # Step 4: Write the modified HTML content to a new HTML file
    print(fileName)
    with open(fileName + ".html", "w", encoding="utf-8") as output_file:
        output_file.write(html_content)
