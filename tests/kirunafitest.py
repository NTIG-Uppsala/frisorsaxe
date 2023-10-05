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
        self.browser.get(path.join(getcwd(), "./kirunafi.html"))

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
        self.browser.get(path.join(getcwd(), "./kirunafi.html"))

    def tearDown(self):
        self.browser.get("about:blank")

    def testTitle(self):
        self.assertEqual("Frisör Saxé", self.browser.title)

    def testMap(self):
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

    def testPrices(self):
        self.assertIn("600", self.browser.page_source)
        self.assertIn("500", self.browser.page_source)
        self.assertIn("200", self.browser.page_source)
        self.assertIn("150", self.browser.page_source)
        self.assertIn("200", self.browser.page_source)
        self.assertIn("560", self.browser.page_source)
        self.assertIn("300", self.browser.page_source)
        self.assertIn("500", self.browser.page_source)

    def testBookedTime(self):
        self.assertIn("Puhelin", self.browser.page_source)  # Phone
        self.assertIn("Sähköposti", self.browser.page_source)  # Email
        self.assertIn("Varaa aika", self.browser.page_source)  # Book an appointment
        self.assertIn("0630‑555‑555", self.browser.page_source)  # Phone number
        self.assertIn("saxefrisor@gmail.com", self.browser.page_source)  # Email address

    def testOpeningHours(self):
        self.assertIn("Ma - Pe", self.browser.page_source)  # Mon - Fri
        self.assertIn("Lauantai", self.browser.page_source)  # Saturday
        self.assertIn("Sunnuntai", self.browser.page_source)  # Sunday
        self.assertIn("Suljettu", self.browser.page_source)  # Closed

    def testInfo(self):
        self.assertIn(
            "Kolmen käynnin jälkeen 12 kuukauden aikana sinut katsotaan vakituiseksi asiakkaaksi",
            self.browser.page_source,
        )  # After three visits within 12 months, you will be considered a regular customer
        self.assertIn(
            "Pitkien hiusten raja alkaa 20 cm:stä", self.browser.page_source
        )  # The limit for long hair starts at 20 cm

    def testProducts(self):
        self.assertIn("Pitkät hiukset", self.browser.page_source)  # Long hair
        self.assertIn("Tänään", self.browser.page_source)  # Today
        self.assertIn("Lyhyet hiukset", self.browser.page_source)  # Short hair
        self.assertIn("Parta", self.browser.page_source)  # Beard
        self.assertIn("Lapsi", self.browser.page_source)  # Children
        self.assertIn("vuotta", self.browser.page_source)  # years
        self.assertIn("Trimmaus", self.browser.page_source)  # Trim
        self.assertIn("Värjäys", self.browser.page_source)  # Coloring
        self.assertIn(
            "Pidennykset, lyhyet", self.browser.page_source
        )  # Short extensions
        self.assertIn(
            "Pidennykset, tavalliset", self.browser.page_source
        )  # Medium-length extensions
        self.assertIn(
            "Pidennykset, pitkät", self.browser.page_source
        )  # Long extensions

    def testNavbar(self):
        navBrand = self.browser.find_element(By.ID, "centerText")
        self.assertIn(
            "Frisör&nbsp;Saxé", navBrand.get_attribute("innerHTML")
        )  # Hairdresser Saxé
        element = self.browser.find_element(By.CLASS_NAME, "navbar-nav")
        self.assertIn(
            "Varaa aika", element.get_attribute("innerHTML")
        )  # Book an appointment
        self.assertIn(
            "Aukioloajat", element.get_attribute("innerHTML")
        )  # Opening hours
        self.assertIn("Hinnat", element.get_attribute("innerHTML"))  # Prices
        self.assertIn("Henkilökunta", element.get_attribute("innerHTML"))  # Staff
        self.assertIn("loyda-meidat", element.get_attribute("innerHTML"))  # Find Us

    def testEmployeeHeader(self):
        self.assertIn(
            "Tapaa henkilökuntaamme", self.browser.page_source
        )  # Meet our staff

    def testEmployeeJobs(self):
        self.assertIn("Parturi", self.browser.page_source)  # Barber
        self.assertIn("Hiusmuotoilija", self.browser.page_source)  # Hair stylist

    def testAddress(self):
        self.assertIn("Osoite", self.browser.page_source)  # Address

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

    def testPostalCodePhrase(self):
        self.assertIn(
            "Ammattimaiset hiustenleikkaukset kotiin", self.browser.page_source
        )

    def helperPostalCode(self, PostalCodeList, message):
        for currentPostalCode in PostalCodeList:
            self.browser.find_element(By.ID, "postalCodeNumber").send_keys(
                currentPostalCode
            )
            time.sleep(0.5)
            self.browser.find_element(By.ID, "submit").click()
            postalOutput = self.browser.find_element(By.ID, "postalCodeCheck")
            self.assertIn(message, postalOutput.text)
            self.browser.get("about:blank")
            self.browser.get(path.join((getcwd()), "./kirunafi.html"))

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
            "Toimitamme kotiin. Soita meille ajanvarauksesta!",
        )
        self.helperPostalCode(
            notAcceptedPostalCodes,
            "Valitettavasti emme voi tarjota tätä palvelua tällä postinumerolla.",
        )
        self.helperPostalCode(nonWorkingPostalCodes, "Ei voimassa oleva postinumero.")

    def testPlaceholderForFileGenerator(self):
        errorMessages = []  # Create a list to collect error messages
        matches = re.findall(
            "\*[A-Z]+\*", self.browser.page_source
        )  # Check if placeholders from template exist.
        for match in matches:
            errorMessages.append(match)  # Append error messages to the list
            print(match)

        if errorMessages:
            # If there are errors, print them and fail the test
            self.fail(errorMessages)

    def helperAreWeOpen(self, date, expectedResult, openTime):
        self.browser.execute_script(f'setOpeningStatus(new Date("{date}"));')
        displayedIfClosed = self.browser.find_element(
            By.ID, "displayedIfClosed"
        ).value_of_css_property("display")
        displayedIfOpen = self.browser.find_element(
            By.ID, "displayedIfOpen"
        ).value_of_css_property("display")
        diplayedIfOpenTom = self.browser.find_element(By.ID, "displayedIfOpenTom")
        displayedIfOpenToDay = self.browser.find_element(By.ID, "displayedIfOpenToDay")
        displayedIfOpenMonday = self.browser.find_element(
            By.ID, "displayedIfOpenMonday"
        )

        if (
            expectedResult == "Closed"
            and displayedIfClosed == "block"
            and displayedIfOpen == "none"
        ):
            if (
                diplayedIfOpenTom.value_of_css_property("display") == "block"
                and displayedIfOpenToDay.value_of_css_property("display") == "none"
                and displayedIfOpenMonday.value_of_css_property("display") == "none"
            ):
                self.assertEqual(
                    diplayedIfOpenTom.text, "Avaamme huomenna klo: " + openTime
                )
            elif (
                displayedIfOpenToDay.value_of_css_property("display") == "block"
                and diplayedIfOpenTom.value_of_css_property("display") == "none"
                and displayedIfOpenMonday.value_of_css_property("display") == "none"
            ):
                self.assertEqual(
                    displayedIfOpenToDay.text, "Avaamme tänään klo: " + openTime
                )
            elif (
                displayedIfOpenMonday.value_of_css_property("display") == "block"
                and displayedIfOpenToDay.value_of_css_property("display") == "none"
                and diplayedIfOpenTom.value_of_css_property("display") == "none"
            ):
                self.assertEqual(
                    displayedIfOpenMonday.text, "Avaamme maanantaina klo: " + openTime
                )
            else:
                self.fail("fel")

        elif (
            expectedResult == "Open"
            and displayedIfClosed == "none"
            and displayedIfOpen == "block"
        ):
            return
        else:
            self.fail("fel2")

    def testAreWeOpen(self):
        # Monday
        self.helperAreWeOpen("2023-10-02T09:59:00", "Closed", "10")
        self.helperAreWeOpen("2023-10-02T10:01:00", "Open", None)
        self.helperAreWeOpen("2023-10-02T15:59:00", "Open", None)
        self.helperAreWeOpen("2023-10-02T16:01:00", "Closed", "10")

        # Tuesday
        self.helperAreWeOpen("2023-10-03T09:59:00", "Closed", "10")
        self.helperAreWeOpen("2023-10-03T10:01:00", "Open", None)
        self.helperAreWeOpen("2023-10-03T15:59:00", "Open", None)
        self.helperAreWeOpen("2023-10-03T16:01:00", "Closed", "10")

        # Wendsday
        self.helperAreWeOpen("2023-10-04T09:59:00", "Closed", "10")
        self.helperAreWeOpen("2023-10-04T10:01:00", "Open", None)
        self.helperAreWeOpen("2023-10-04T15:59:00", "Open", None)
        self.helperAreWeOpen("2023-10-04T16:01:00", "Closed", "10")

        # Thursday
        self.helperAreWeOpen("2023-10-05T09:59:00", "Closed", "10")
        self.helperAreWeOpen("2023-10-05T10:01:00", "Open", None)
        self.helperAreWeOpen("2023-10-05T15:59:00", "Open", None)
        self.helperAreWeOpen("2023-10-05T16:01:00", "Closed", "10")

        # Friday
        self.helperAreWeOpen("2023-10-06T09:59:00", "Closed", "10")
        self.helperAreWeOpen("2023-10-06T10:01:00", "Open", None)
        self.helperAreWeOpen("2023-10-06T15:59:00", "Open", None)
        self.helperAreWeOpen("2023-10-06T16:01:00", "Closed", "12")

        # Saturday
        self.helperAreWeOpen("2023-10-07T11:59:00", "Closed", "12")
        self.helperAreWeOpen("2023-10-07T12:01:00", "Open", None)
        self.helperAreWeOpen("2023-10-07T14:59:00", "Open", None)
        self.helperAreWeOpen("2023-10-07T15:01:00", "Closed", "10")

        # Sunday
        self.helperAreWeOpen("2023-10-08T09:59:00", "Closed", "10")
        self.helperAreWeOpen("2023-10-08T12:01:00", "Closed", "10")
        self.helperAreWeOpen("2023-10-08T14:59:00", "Closed", "10")
        self.helperAreWeOpen("2023-10-08T15:01:00", "Closed", "10")


if __name__ == "__main__":
    main(verbosity=2)
