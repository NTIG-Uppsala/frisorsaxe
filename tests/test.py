import time
from os import getcwd, path
from unittest import TestCase, main

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestHomepageNoScript(TestCase):
    doNotCloseBrowser = False
    hideWindow = False

    # setUpClass körs FÖRE DET FÖRSTA testet
    @classmethod
    def setUpClass(cls):
        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_experimental_option(
            "prefs", {"profile.managed_default_content_settings.javascript": 2}
        )

        if cls.doNotCloseBrowser:
            chrome_options.add_experimental_option("detach", True)

        if cls.hideWindow:
            chrome_options.add_argument("--headless")

        cls.browser = webdriver.Chrome(options=chrome_options)

    # After last test
    @classmethod
    def tearDownClass(cls):
        pass

    # Runs before every test
    def setUp(self):
        self.browser.get(path.join(getcwd(), "index.html"))

    # After each test
    def tear_down(self):
        self.browser.get("about:blank")

    def testNoScriptImage(self):
        image_elements = self.browser.find_elements(By.TAG_NAME, "img")

        for image_element in image_elements:
            is_loaded = self.browser.execute_script(
                "return arguments[0].complete && typeof arguments[0].naturalWidth != 'undefined' && arguments[0].naturalWidth > 0;",
                image_element,
            )

            if is_loaded:
                print(f"Image '{image_element.get_attribute('src')}' is loaded.")
            else:
                self.fail(
                    f"Image '{image_element.get_attribute('src')}' is not loaded."
                )


class TestHomepage(TestCase):
    doNotCloseBrowser = False
    hideWindow = False

    # setUpClass körs FÖRE DET FÖRSTA testet
    @classmethod
    def setUpClass(cls):
        chr_options = Options()

        if cls.doNotCloseBrowser:
            chr_options.add_experimental_option("detach", True)

        if cls.hideWindow:
            chr_options.add_argument("--headless")

        cls.browser = webdriver.Chrome(options=chr_options)

    # After last test
    @classmethod
    def tearDownClass(cls):
        pass

    # Runs before every test
    def setUp(self):
        self.browser.get(path.join(getcwd(), "index.html"))

    # After each test
    def tear_down(self):
        self.browser.get("about:blank")

    def testTitle(self):
        self.assertEqual("Frisör Saxé", self.browser.title)

    def testMap(self):
        self.browser.find_element(By.ID, "map")
        self.assertIn(
            "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d1503.2583513342254!2d20.2337795!3d67.8660232!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x45d0ba6368d7c9a3%3A0xe3887ef038c559b0!2sFj%C3%A4llgatan%2032%2C%20981%2039%20Kiruna!5e0!3m2!1ssv!2sse!4v1693397051519!5m2!1ssv!2sse",
            self.browser.page_source,
        )

    def testImageLoading(self):
        image_elements = self.browser.find_elements(By.TAG_NAME, "img")

        for image_element in image_elements:
            is_loaded = self.browser.execute_script(
                "return arguments[0].complete && typeof arguments[0].naturalWidth != 'undefined' && arguments[0].naturalWidth > 0;",
                image_element,
            )

            if is_loaded:
                print(f"Image '{image_element.get_attribute('src')}' is loaded.")
            else:
                self.fail(
                    f"Image '{image_element.get_attribute('src')}' is not loaded."
                )

    def testBookedTime(self):
        self.assertIn("Boka tid", self.browser.page_source)
        self.assertIn("Telefon", self.browser.page_source)
        self.assertIn("Mail", self.browser.page_source)
        self.assertIn("0630-555-555", self.browser.page_source)
        self.assertIn("info@ntig-uppsala.github.io", self.browser.page_source)

    def testOppeningHours(self):
        self.assertIn("Öppettider", self.browser.page_source)
        self.assertIn("Mån", self.browser.page_source)
        self.assertIn("Fre", self.browser.page_source)
        self.assertIn("Lördag", self.browser.page_source)
        self.assertIn("Söndag", self.browser.page_source)
        self.assertIn("Stängt", self.browser.page_source)
        self.browser.find_element(By.ID, "vardagar")

    def testProducts(self):
        self.assertIn("Klippning", self.browser.page_source)
        self.assertIn("Långt", self.browser.page_source)
        self.assertIn("Övrigt", self.browser.page_source)
        self.assertIn("Färgning", self.browser.page_source)
        self.assertIn("Extensions", self.browser.page_source)
        self.assertIn("Kort", self.browser.page_source)
        self.assertIn("Skägg", self.browser.page_source)
        self.assertIn("Barn", self.browser.page_source)
        self.assertIn("Toppning", self.browser.page_source)
        self.assertIn("stamkund", self.browser.page_source)
        self.assertIn("hår", self.browser.page_source)

    def testNavbar(self):
        nabBrand = self.browser.find_element(By.ID, "centerText")
        self.assertIn("Frisör&nbsp;Saxé", nabBrand.get_attribute("innerHTML"))
        element = self.browser.find_element(By.CLASS_NAME, "navbar-nav")
        self.assertIn("Boka&nbsp;tid", element.get_attribute("innerHTML"))
        self.assertIn("Öppettider", element.get_attribute("innerHTML"))
        self.assertIn("Priser", element.get_attribute("innerHTML"))
        self.assertIn("Personal", element.get_attribute("innerHTML"))
        self.assertIn("Hitta&nbsp;oss", element.get_attribute("innerHTML"))

    def testHeadHeader(self):
        self.assertIn("Möt vår personal", self.browser.page_source)

    def testDesktopScreenshots(self):
        time.sleep(2)
        self.browser.save_screenshot("../ss/ss_home.png")

        self.browser.find_element(By.LINK_TEXT, "Priser").click()
        time.sleep(2)
        self.browser.save_screenshot("../ss/ss_prices.png")

        self.browser.get(path.join(getcwd(), "index.html"))
        self.browser.find_element(By.LINK_TEXT, "Hitta oss").click()
        time.sleep(2)
        self.browser.save_screenshot("../ss/ss_map.png")

    def testMobileScreenshot(self):
        mobile_emulation = {"deviceName": "iPhone X"}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        # Mobile simulation
        self.browser = webdriver.Chrome(options=chrome_options)

        self.browser.get(path.join(getcwd(), "index.html"))
        self.browser.save_screenshot("../ss/ss_hem_mobil.png")

    def testEmployeePictures(self):
        self.assertIn('alt="Örjan"', self.browser.page_source)
        self.assertIn('alt="Fredrik"', self.browser.page_source)
        self.assertIn('alt="Anna"', self.browser.page_source)


if __name__ == "__main__":
    main(verbosity=2)
