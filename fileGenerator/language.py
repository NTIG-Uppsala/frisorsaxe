# Step 1: Read and parse the HTML file
with open("fileGenerator/template.html", "r", encoding="utf-8") as html_file:
    html_content = html_file.read()

outputNumber = 0

languages = [
    "fileGenerator/kirunaeng.txt",
    "fileGenerator/kirunaswe.txt",
    "fileGenerator/luleåeng.txt",
    "fileGenerator/luleåswe.txt",
]
output = [
    "testkirunaeng.html",
    "testkirunaswe.html",
    "testluleaeng.html",
    "testluleaswe.html",
]
# Step 2: Read the text document with variable replacements
for language in languages:
    with open(language, "r", encoding="utf-8") as variables_file:
        variables = {}
        for line in variables_file:
            key, value = line.strip().split("|")
            variables[key] = value

    # Step 3: Replace variables in the HTML content
    for variable, value in variables.items():
        html_content = html_content.replace(f"^{variable}^", value)
        html_content = html_content.replace(f"*{variable}*", value)

    # Step 4: Write the modified HTML content to a new HTML file
    with open(output[outputNumber], "w", encoding="utf-8") as output_file:
        output_file.write(html_content)
    outputNumber += 1

print("HTML file with variables replaced has been generated as 'output.html'")
