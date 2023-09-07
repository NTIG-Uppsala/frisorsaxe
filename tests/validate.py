import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

URL = "https://validator.w3.org/nu/"

chrome_options = Options()
# prevents chrome from closing when done, from https://stackoverflow.com/a/51865955
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=chrome_options)

# get all file paths
paths = []


for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        paths.append(os.path.join(root, name))
    for name in dirs:
        paths.append(os.path.join(root, name))

TABS_OPEN = 1
failed_validations_count = 0

# loop through file paths and validate the files
for path in paths:
    if not (path.endswith(".html") or path.endswith(".css")):
        continue

    # open a new tab and switch to it
    browser.execute_script("window.open('');")
    TABS_OPEN += 1
    browser.switch_to.window(browser.window_handles[TABS_OPEN - 1])
    # open the validation website
    browser.get(URL)
    # change dropdown to "file upload"
    docselector = browser.find_element(By.ID, "docselect")
    select = Select(docselector)
    select.select_by_visible_text("file upload")
    # upload and submit file
    file_upload_button = browser.find_element(By.ID, "doc")
    file_upload_button.send_keys(os.path.abspath(path))
    check_button = browser.find_element(By.ID, "submit")
    check_button.click()

    # check if the uploaded file passed the validation
    if '<div id="results"><p class="success">' in browser.page_source:
        print(path, "passed")
    else:
        print(path, "failed")
        failed_validations_count += 1

if failed_validations_count > 0:
    raise Exception("validation failed")
