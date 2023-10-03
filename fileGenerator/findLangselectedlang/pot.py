import json

jsonFile = json.load(open("fileGenerator/findLangselectedlang/data.json"))

selectedLanguage = ["en", "sv", "fi"]  # Change this to the desired language
selectedLocation = ["LULEA", "KIRUNA"]


location_names = list(jsonFile["Locations"].keys())
for location in location_names:
    print(location)
