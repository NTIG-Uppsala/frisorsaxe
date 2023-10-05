import re
import time
from os import getcwd, path
from unittest import TestCase, main

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestHomepageNoScriptENG(TestCase):
    doNotCloseBrowser = False
    hideWindow = False

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

    @classmethod
    def tearDownClass(cls):
        pass

    # Before each test
    def setUp(self):
        self.browser.get(path.join(getcwd(), "./kirunaen.html"))

    # After each test
    def tearDown(self):
        self.browser.get("about:blank")

    def testNoScriptImage(self):
        image_elements = self.browser.find_elements(By.TAG_NAME, "img")

        for image_element in image_elements:
            is_loaded = self.browser.execute_script(
                "return arguments[0].complete && typeof arguments[0].naturalWidth != 'undefined' && arguments[0].naturalWidth > 0;",  ##The pictures exists, has a naturalwidth and its longer then 0
                image_element,
            )

            if is_loaded:
                print(f"Image '{image_element.get_attribute('src')}' is loaded.")
                print(image_element)
            else:
                print(image_element)
                self.fail(
                    f"Image '{image_element.get_attribute('src')}' is not loaded."
                )


class TestHomepageENG(TestCase):
    doNotCloseBrowser = False
    hideWindow = True

    @classmethod
    def setUpClass(cls):
        chr_options = Options()

        if cls.doNotCloseBrowser:
            chr_options.add_experimental_option("detach", True)

        if cls.hideWindow:
            chr_options.add_argument("--headless")

        cls.browser = webdriver.Chrome(options=chr_options)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.browser.get(path.join(getcwd(), "./kirunaen.html"))

    def tearDown(self):
        self.browser.get("about:blank")

    def testTitle(self):
        self.assertEqual("Frisör Saxé", self.browser.title)

    def testMap(self):
        self.browser.find_element(By.ID, "findus")
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

        self.assertIn("600", self.browser.page_source)
        self.assertIn("500", self.browser.page_source)
        self.assertIn("200", self.browser.page_source)
        self.assertIn("150", self.browser.page_source)
        self.assertIn("200", self.browser.page_source)
        self.assertIn("560", self.browser.page_source)
        self.assertIn("300", self.browser.page_source)
        self.assertIn("500", self.browser.page_source)

    def testBookedTime(self):
        self.assertIn("Appointment", self.browser.page_source)
        self.assertIn("Phone", self.browser.page_source)
        self.assertIn("Email", self.browser.page_source)
        self.assertIn("0630‑555‑555", self.browser.page_source)
        self.assertIn("saxefrisor@gmail.com", self.browser.page_source)

    def testOpeningHours(self):
        self.assertIn("Opening Hours", self.browser.page_source)
        self.assertIn("Mon", self.browser.page_source)
        self.assertIn("Fri", self.browser.page_source)
        self.assertIn("Saturday", self.browser.page_source)
        self.assertIn("Sunday", self.browser.page_source)
        self.assertIn("Closed", self.browser.page_source)

    def testInfo(self):
        self.assertIn(
            "After 3 visits within 12 months you are considered a regular customer",
            self.browser.page_source,
        )
        self.assertIn(
            "The limit for long hair starts at 20 cm", self.browser.page_source
        )

    def testProducts(self):
        self.assertIn("Haircut", self.browser.page_source)
        self.assertIn("Long", self.browser.page_source)
        self.assertIn("Other", self.browser.page_source)
        self.assertIn("Coloring", self.browser.page_source)
        self.assertIn("Extensions", self.browser.page_source)
        self.assertIn("Short", self.browser.page_source)
        self.assertIn("Beard", self.browser.page_source)
        self.assertIn("Children", self.browser.page_source)
        self.assertIn("Trimming", self.browser.page_source)
        self.assertIn("regular&nbsp;customer", self.browser.page_source)
        self.assertIn("hair", self.browser.page_source)
        self.assertIn("Beard (20&nbsp;min)", self.browser.page_source)

    def testNavbar(self):
        navBrand = self.browser.find_element(By.ID, "centerText")
        self.assertIn("Frisör&nbsp;Saxé", navBrand.get_attribute("innerHTML"))
        element = self.browser.find_element(By.CLASS_NAME, "navbar-nav")
        self.assertIn("Appointment", element.get_attribute("innerHTML"))
        self.assertIn("Opening Hours", element.get_attribute("innerHTML"))
        self.assertIn("Prices", element.get_attribute("innerHTML"))
        self.assertIn("Staff", element.get_attribute("innerHTML"))
        self.assertIn("Find Us", element.get_attribute("innerHTML"))

    def testEmployeeHeader(self):
        self.assertIn("Meet Our Staff", self.browser.page_source)

    def testEmployeePictures(self):
        self.assertIn('alt="Örjan Johansson"', self.browser.page_source)
        self.assertIn('alt="Fredrik Örtqvist"', self.browser.page_source)
        self.assertIn('alt="Anna Pettersson"', self.browser.page_source)

    def testEmployeeJobs(self):
        self.assertIn("Hairstylist", self.browser.page_source)
        self.assertIn("Barber", self.browser.page_source)

    def testAddress(self):
        self.assertIn("Address", self.browser.page_source)

    def testDailySales(self):
        self.helpTestDailySales("2023-09-11T11:00:00", "saleLongHair")  # Monday
        self.helpTestDailySales("2023-09-12T11:00:00", "saleShortHair")  # Tuesday
        self.helpTestDailySales("2023-09-13T11:00:00", "saleBeard")  # Wednesday
        self.helpTestDailySales("2023-09-14T11:00:00", "saleColoring")  # Thursday

        # Put in the id of the sale that is supposed to show, in the second parameter.
        self.helpDailySalesNotShow("2023-09-11T11:00:00", "saleLongHair")  # On Monday
        self.helpDailySalesNotShow("2023-09-12T11:00:00", "saleShortHair")  # On Tuesday
        self.helpDailySalesNotShow("2023-09-13T11:00:00", "saleBeard")  # On Wednesday
        self.helpDailySalesNotShow("2023-09-14T11:00:00", "saleColoring")  # On Thursday
        self.helpDailySalesNotShow("2023-09-15T11:00:00", "")  # On Friday
        self.helpDailySalesNotShow("2023-09-16T11:00:00", "")  # On Saturday
        self.helpDailySalesNotShow("2023-09-17T11:00:00", "")  # On Sunday

    def helpTestDailySales(self, date, id):
        self.browser.execute_script("dailySales(new Date('" + date + "'))")
        element = self.browser.find_element(By.ID, id).value_of_css_property("display")
        self.assertEqual("block", element)

    def helpDailySalesNotShow(self, date, expectedToShow):
        self.browser.execute_script("dailySales(new Date('" + date + "'))")
        ids = ["saleBeard", "saleColoring", "saleLongHair", "saleShortHair"]
        # Removes the id that is supposed to be showing from the list
        if expectedToShow in ids:
            ids.remove(expectedToShow)
        elif expectedToShow == "":
            pass
        else:
            self.fail()
        # Checks that non of the ids in the list is showing
        for id in ids:
            element = self.browser.find_element(By.ID, id).value_of_css_property(
                "display"
            )
            self.assertEqual("none", element)

    def helperPostalCode(self, postalCodeList, message):
        for currentPostalCode in postalCodeList:
            self.browser.find_element(By.ID, "postalCodeNumber").send_keys(
                currentPostalCode
            )
            time.sleep(0.5)
            self.browser.find_element(By.ID, "submit").click()
            postalOutput = self.browser.find_element(By.ID, "postalCodeCheck")
            self.assertIn(message, postalOutput.text)
            self.browser.get("about:blank")
            self.browser.get(path.join((getcwd()), "kirunaen.html"))

        # Bring the value of HOMEDELIVERYTITLE and check

    def testPostalCodePhrase(self):
        self.assertIn("Bring the Salon to Your Home", self.browser.page_source)

    def testPostalCodes(self):
        postalCodeListKiruna = [
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
        notAcceptedPostalCodes = [
            "12345",
            "55555",
            "92347",
        ]
        nonWorkingPostalCodes = [
            "1234",
            "hej",
            "xxxxx",
        ]
        self.helperPostalCode(
            postalCodeListKiruna,
            "You are within reach. Call us to book a house appointment!",
        )
        self.helperPostalCode(
            notAcceptedPostalCodes,
            "Sorry, we can't offer this service for your location.",
        )
        self.helperPostalCode(nonWorkingPostalCodes, "Not a valid postal code.")

    def testPlaceholderForFileGenerator(self):
        errorMessages = []  # Create a list to collect error messages
        matches = re.findall("\*[A-Z]+\*", self.browser.page_source)
        for match in matches:
            errorMessages.append(match)  # Append error messages to the list
            print(match)

        if errorMessages:
            # If there are errors, print them and fail the test
            self.fail(errorMessages)

    def helperWeAreCurrently(self, date, expectedResult):
        self.browser.execute_script(f'setOpeningStatus(new Date("{date}"));')
        displayedIfClosed = self.browser.find_element(
            By.ID, "displayedIfClosed"
        ).value_of_css_property("display")
        displayedIfOpen = self.browser.find_element(
            By.ID, "displayedIfOpen"
        ).value_of_css_property("display")

        if (
            expectedResult == "Closed"
            and displayedIfClosed == "block"
            and displayedIfOpen == "none"
        ):
            return
        elif (
            expectedResult == "Open"
            and displayedIfClosed == "none"
            and displayedIfOpen == "block"
        ):
            return
        else:
            self.fail("fel")

    def testWeAreCurrently(self):
        # Monday
        self.helperWeAreCurrently("2023-10-02T09:59:00", "Closed")
        self.helperWeAreCurrently("2023-10-02T10:01:00", "Open")
        self.helperWeAreCurrently("2023-10-02T15:59:00", "Open")
        self.helperWeAreCurrently("2023-10-02T16:01:00", "Closed")

        # Tuesday
        self.helperWeAreCurrently("2023-10-03T09:59:00", "Closed")
        self.helperWeAreCurrently("2023-10-03T10:01:00", "Open")
        self.helperWeAreCurrently("2023-10-03T15:59:00", "Open")
        self.helperWeAreCurrently("2023-10-03T16:01:00", "Closed")

        # Wendsday
        self.helperWeAreCurrently("2023-10-04T09:59:00", "Closed")
        self.helperWeAreCurrently("2023-10-04T10:01:00", "Open")
        self.helperWeAreCurrently("2023-10-04T15:59:00", "Open")
        self.helperWeAreCurrently("2023-10-04T16:01:00", "Closed")

        # Thursday
        self.helperWeAreCurrently("2023-10-05T09:59:00", "Closed")
        self.helperWeAreCurrently("2023-10-05T10:01:00", "Open")
        self.helperWeAreCurrently("2023-10-05T15:59:00", "Open")
        self.helperWeAreCurrently("2023-10-05T16:01:00", "Closed")

        # Friday
        self.helperWeAreCurrently("2023-10-06T09:59:00", "Closed")
        self.helperWeAreCurrently("2023-10-06T10:01:00", "Open")
        self.helperWeAreCurrently("2023-10-06T15:59:00", "Open")
        self.helperWeAreCurrently("2023-10-06T16:01:00", "Closed")

        # Saturday
        self.helperWeAreCurrently("2023-10-07T11:59:00", "Closed")
        self.helperWeAreCurrently("2023-10-07T12:01:00", "Open")
        self.helperWeAreCurrently("2023-10-07T14:59:00", "Open")
        self.helperWeAreCurrently("2023-10-07T15:01:00", "Closed")


if __name__ == "__main__":
    main(verbosity=2)
