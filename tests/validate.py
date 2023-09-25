import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
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
checkbox_checked = False

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        paths.append(os.path.join(root, name))
    for name in dirs:
        paths.append(os.path.join(root, name))

TABS_OPEN = 1
failed_validations_count = 0

# Loop through file paths and validate the files
for path in paths:
    if not (path.endswith(".html") or path.endswith(".css")):
        continue

    # Open a new tab and switch to it
    browser.execute_script("window.open('');")
    TABS_OPEN += 1
    browser.switch_to.window(browser.window_handles[TABS_OPEN - 1])
    # Open the validation website
    browser.get(URL)
    # Change dropdown to "file upload"
    docselector = browser.find_element(By.ID, "docselect")
    select = Select(docselector)
    select.select_by_visible_text("file upload")
    # Upload and submit file
    browser.find_element(By.ID, "doc").send_keys(os.path.abspath(path))
    browser.find_element(By.ID, "submit").click()
    # Remove inputmode warning
    if checkbox_checked != True:  # only executes if inputmode isnt checked off
        try:
            # Checks if messages filtering is available
            browser.find_element(By.XPATH, '//*[@id="filters"]/h2/button')
        except NoSuchElementException:
            continue
        else:
            # Opens messages filtering
            browser.find_element(By.XPATH, '//*[@id="filters"]/h2/button').click()
            # Locates the inputmode warning and then unchecks the checkbox
            code_elements = browser.find_elements(By.XPATH, "//code")
            for code_element in code_elements:
                if code_element.text == "inputmode":
                    grandparent_element = code_element.find_element(
                        By.XPATH, "../../.."
                    )
                    time.sleep(1)
                    grandparent_element.find_element(
                        By.XPATH, './/input[@type="checkbox"]'
                    ).click()
                    checkbox_checked = True
                    break
            for code_element in code_elements:
                if code_element.text == "*HTMLLANGUAGE*":
                    grandparent_element = code_element.find_element(
                        By.XPATH, "../../.."
                    )
                    time.sleep(1)
                    grandparent_element.find_element(
                        By.XPATH, './/input[@type="checkbox"]'
                    ).click()
                    checkbox_checked = True
                    break
