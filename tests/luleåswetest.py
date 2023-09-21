import time
from os import getcwd, path
from unittest import TestCase, main

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestHomepageNoScript(TestCase):
    doNotCloseBrowser = False
    hideWindow = False

    # Runs before the first test
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
        self.browser.get(path.join(getcwd(), "luleaswe.html"))

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
    hideWindow = True

    # Runs before the first test
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
        self.browser.get(path.join(getcwd(), "luleaswe.html"))

    # After each test
    def tearDown(self):
        self.browser.get("about:blank")

    def testTitle(self):
        self.assertEqual("Frisör Saxé", self.browser.title)

    def testMap(self):
        self.browser.find_element(By.ID, "hittaoss")
        self.assertIn(
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1643.085861319367!2d21.851066699999997!3d65.68080189999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x467f677c34b6b1af%3A0x493f441e2dee92f!2sF%C3%A4rjledsv%C3%A4gen%2038%2C%20961%2093%20S%C3%B6dra%20Sunderbyn!5e0!3m2!1ssv!2sse!4v1694676621148!5m2!1ssv!2sse",
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
        self.assertIn("Boka&nbsp;tid", self.browser.page_source)
        self.assertIn("Telefon", self.browser.page_source)
        self.assertIn("E‑post", self.browser.page_source)
        self.assertIn("0640‑555‑333", self.browser.page_source)
        self.assertIn("lulea@ntig-uppsala.github.io", self.browser.page_source)

    def testPrices(self):
        self.assertIn("600", self.browser.page_source)
        self.assertIn("500", self.browser.page_source)
        self.assertIn("200", self.browser.page_source)
        self.assertIn("150", self.browser.page_source)
        self.assertIn("200", self.browser.page_source)
        self.assertIn("560", self.browser.page_source)
        self.assertIn("300 ", self.browser.page_source)
        self.assertIn("500", self.browser.page_source)

    def testDailySales(self):
        self.helpTestDailySales("2023-09-11T11:00:00", "saleLongHair")  # Monday
        self.helpTestDailySales("2023-09-12T11:00:00", "saleShortHair")  # Tuesday
        self.helpTestDailySales("2023-09-13T11:00:00", "saleBeard")  # Wednesday
        self.helpTestDailySales("2023-09-14T11:00:00", "saleColoring")  # Thursday

        # Should not show
        self.helpDailySalesNotShow("2023-09-12T11:00:00", "saleLongHair")  # On tuseday
        self.helpDailySalesNotShow("2023-09-11T11:00:00", "saleShortHair")  # On Monday
        self.helpDailySalesNotShow(
            "2023-09-13T11:00:00", "saleColoring"
        )  # On wednesday
        self.helpDailySalesNotShow(
            "2023-09-13T11:00:00", "saleLongHair"
        )  # On wednesday
        self.helpDailySalesNotShow("2023-09-11T16:00:00", "saleColoring")  # On Monday
        self.helpDailySalesNotShow("2023-09-11T09:00:00", "saleLongHair")  # On Monday

    def helpTestDailySales(self, date, id):
        self.browser.execute_script("dailySales(new Date('" + date + "'))")
        element = self.browser.find_element(By.ID, id).value_of_css_property("display")
        if element == "block":
            pass
        else:
            self.fail()

    def helpDailySalesNotShow(self, date, id):
        self.browser.get(path.join(getcwd(), "luleaswe.html"))
        self.browser.execute_script("dailySales(new Date('" + date + "'))")
        element = self.browser.find_element(By.ID, id).value_of_css_property("display")
        if element == "none":
            pass
        else:
            self.fail()

    def testOppeningHours(self):
        self.assertIn("Öppettider", self.browser.page_source)
        self.assertIn("Mån", self.browser.page_source)
        self.assertIn("Fre", self.browser.page_source)
        self.assertIn("Lördag", self.browser.page_source)
        self.assertIn("Söndag", self.browser.page_source)
        self.assertIn("Stängt", self.browser.page_source)

    def testInfo(self):
        self.assertIn("Gränsen för långt hår går vid 20cm", self.browser.page_source)
        self.assertIn(
            "Man blir stamkund efter tre besök under 12 månader",
            self.browser.page_source,
        )

    def testProducts(self):
        self.assertIn("Klippning", self.browser.page_source)
        self.assertIn("Långt", self.browser.page_source)
        self.assertIn("Annat", self.browser.page_source)
        self.assertIn("Färgning", self.browser.page_source)
        self.assertIn("Förlängningar", self.browser.page_source)
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

    def testEmployeeHeader(self):
        self.assertIn("Möt vår personal", self.browser.page_source)

    def testEmployeePictures(self):
        self.assertIn('alt="Johan Olsson"', self.browser.page_source)
        self.assertIn('alt="Anna Andersson"', self.browser.page_source)
        self.assertIn('alt="Elin Nygård"', self.browser.page_source)

    def testEmployeeJobs(self):
        self.assertIn("Hårstylist", self.browser.page_source)
        self.assertIn("Barberare", self.browser.page_source)

    def testAddress(self):
        self.assertIn("Adress", self.browser.page_source)

    def helperZipCode(self, zipCodeList, message):
        for currentZip in zipCodeList:
            self.browser.find_element(By.ID, "zipNumber").send_keys(currentZip)
            time.sleep(0.5)
            self.browser.find_element(By.ID, "submit").click()
            zipOutput = self.browser.find_element(By.ID, "zipCodeCheck")
            self.assertIn(message, zipOutput.text)
            self.browser.get("about:blank")
            self.browser.get(path.join((getcwd()), "index.html"))

    def testZipCodes(self):
        validZipcodes = [
            "98132",
            "98135",
            "98136",
            "98137",
            "98138",
            "98139",
            "98140",
            "98142",
            "98143",
            "98144",
            "98146",
            "98147",
        ]
        notAcceptedZipcodes = [
            "12345",
            "55555",
            "92347",
        ]
        nonWorkingZipcodes = [
            "1234",
            "hej",
            "xxxxx",
        ]
        self.helperZipCode(validZipcodes, "Vi kör ut, ring telefonnumret ovan!")
        self.helperZipCode(notAcceptedZipcodes, "Vi kör tyvärr inte ut till dig.")
        self.helperZipCode(nonWorkingZipcodes, "Inte ett giltigt postnummer.")


if __name__ == "__main__":
    main(verbosity=2)
