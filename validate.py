# importing the requests library
import requests

# api-endpoint
URL = "https://validator.w3.org/nu/"

file_contents = ""

with open("index.html", "r") as file:
    file_contents += file.read()

s = requests.session()

s.headers = {
    "Accept": "text/html",
    "Content-Type": "text/html"
}

response = s.post(URL, data=file_contents)

if "<div id=\"results\"><p class=\"success\">" in response.text:
    print("success")
else:
    print("fail")

with open("output.html", "w", encoding="utf-8") as file:
    file.write(response.text)
