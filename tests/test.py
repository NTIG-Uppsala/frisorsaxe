import time
from os import getcwd, path
from unittest import TestCase, main

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


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
        nabBrand = self.browser.find_element(By.ID, "brandName")
        self.assertIn("Frisör&nbsp;Saxé", nabBrand.get_attribute("innerHTML"))
        element = self.browser.find_element(By.CLASS_NAME, "navbar-collapse")
        self.assertIn("Boka&nbsp;tid", element.get_attribute("innerHTML"))
        self.assertIn("Öppettider", element.get_attribute("innerHTML"))
        self.assertIn("Priser", element.get_attribute("innerHTML"))
        self.assertIn("Personal", element.get_attribute("innerHTML"))
        self.assertIn("Hitta&nbsp;oss", element.get_attribute("innerHTML"))

    def testHeadHeader(self):
        self.assertIn("Lyx och skönhet", self.browser.page_source)
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
