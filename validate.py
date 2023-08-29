from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

URL = "https://validator.w3.org/nu/"

chrome_options = Options()
# Prevents chrome from closing when done, from https://stackoverflow.com/a/51865955
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=chrome_options)

# Get all file paths
paths = []
import os
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
        paths.append(os.path.join(root, name))
   for name in dirs:
        paths.append(os.path.join(root, name))

tabs_open = 1

# Loop through file paths and validate the files
for path in paths:
    mime_type = ""
    if path.endswith("_error.html"):
        continue
    if path.endswith(".html"):
        mime_type = "text/html"
    elif path.endswith(".css"):
        mime_type = "text/css"
    else:
        continue

    # Open a new tab and switch to it
    browser.execute_script("window.open('');")
    tabs_open += 1
    browser.switch_to.window(browser.window_handles[tabs_open - 1])
    # Open the validation website
    browser.get(URL)
    # Change dropdown to "file upload"
    docselector = browser.find_element(By.ID, "docselect")
    select = Select(docselector)
    select.select_by_visible_text("file upload")
    # Upload and submit file
    file_upload_button = browser.find_element(By.ID, "doc")
    file_upload_button.send_keys(os.path.abspath(path))
    check_button = browser.find_element(By.ID, "submit")
    check_button.click()

    # Check if the uploaded file passed the validation
    if "<div id=\"results\"><p class=\"success\">" in browser.page_source:
        print(path, "passed")
    else:
        print(path, "failed")

