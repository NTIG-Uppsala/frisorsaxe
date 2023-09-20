import math
import time
from os import getcwd, mkdir, path
from unittest import TestCase, main

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class screenshotNoJs(TestCase):
    doNotCloseBrowser = True
    hideWindow = True

    @classmethod
    def setUpClass(cls):
        chrome_options = webdriver.ChromeOptions()

        if cls.doNotCloseBrowser:
            chrome_options.add_experimental_option("detach", True)

        if cls.hideWindow:
            chrome_options.add_argument("--headless=new")

        chrome_options.add_experimental_option(
            "prefs", {"profile.managed_default_content_settings.javascript": 2}
        )

        cls.browser = webdriver.Chrome(options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.browser.get(path.join(getcwd(), "kirunaswe.html"))

    def tearDown(self):
        self.browser.get("about:blank")

    def screenshotHelper(
        self, width, height
    ):  # Function that defines resolution and takes screenshot.
        self.browser.set_window_size(width, height)

        scroll_height = self.browser.execute_script("return document.body.scrollHeight")
        if scroll_height > height:
            if height >= 1080:
                num_scrolls = (
                    int(scroll_height / height) + 1
                )  # Calculate the number of scrolls needed on bigger screens
            else:
                num_scrolls = int(
                    scroll_height / height
                )  # Calculate the number of scrolls needed

            for i in range(num_scrolls):
                scroll_position = i * height
                self.browser.execute_script(f"window.scrollTo(0, {scroll_position});")
                self.browser.save_screenshot(
                    f"screenshotsnojs/{width}-{height}-{i}a.png"
                )

                scroll_position = (i * height) + (height / 2)
                self.browser.execute_script(f"window.scrollTo(0, {scroll_position});")
                self.browser.save_screenshot(
                    f"screenshotsnojs/{width}-{height}-{i}b.png"
                )
        else:
            # If the page content fits in a single view, capture a screenshot of the entire page.
            self.browser.save_screenshot(f"screenshotsnojs/{width}-{height}-0.png")

    def testScreenshotsNoJs(
        self,
    ):
        if not path.exists("screenshotsnojs/"):
            mkdir("screenshotsnojs/")
        # Phones and tablets
        self.screenshotHelper(360, 740)
        self.screenshotHelper(414, 896)
        # Desktop
        self.screenshotHelper(1024, 768)
        self.screenshotHelper(1920, 1080)
        self.screenshotHelper(3840, 2160)


class screenshot(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()
        chr_options = Options()

        chr_options.headless = True

        cls.browser = webdriver.Chrome(options=chr_options)

    def setUp(self):
        self.browser.get(path.join(getcwd(), "kirunaswe.html"))

    def tearDown(self):
        self.browser.get("about:blank")

    def screenshotHelper(
        self, width, height
    ):  # Includes essential values for taking screenshots. to not have repetetive code.
        self.browser.set_window_size(width, height)
        p_height = self.browser.execute_script("return document.body.scrollHeight")
        if p_height > height:
            scroll_amount = math.ceil(p_height / height)
        else:
            scroll_amount = 1
        for i in range(scroll_amount):
            self.browser.execute_script(f"window.scrollTo(0, window.innerHeight*{i});")
            time.sleep(1)
            self.browser.save_screenshot(f"screenshots/{width}-{height}-{i}.png")

    def testScreenshots(self):  # Function that defines resolution and takes screenshot.
        if not path.exists("screenshots/"):
            mkdir("screenshots/")
        # Phones and tablets
        self.screenshotHelper(360, 740)
        self.screenshotHelper(414, 896)
        # Desktop
        self.screenshotHelper(1024, 768)
        self.screenshotHelper(1920, 1080)
        self.screenshotHelper(3840, 2160)


if __name__ == "__main__":
    main(verbosity=2)
