import re
import time
from os import getcwd, path
from unittest import TestCase, main

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestHomepageNoScriptENG(TestCase):
    doNotCloseBrowser = False
    hideWindow = True

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

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.browser.get(path.join(getcwd(), "./luleaen.html"))

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
            else:
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

    # Before each test
    def setUp(self):
        self.browser.get(path.join(getcwd(), "./luleaen.html"))

    # After each test
    def tearDown(self):
        self.browser.get("about:blank")

    def testTitle(self):
        self.assertEqual("Frisör Saxé", self.browser.title)

    def testMap(self):
        self.browser.find_element(By.ID, "findus")
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
        self.assertIn("Appointment", self.browser.page_source)
        self.assertIn("Phone", self.browser.page_source)
        self.assertIn("Email", self.browser.page_source)
        self.assertIn("0640‑555‑333", self.browser.page_source)
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
        self.assertIn("Beard", self.browser.page_source)

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
        self.assertIn('alt="Johan Olsson"', self.browser.page_source)
        self.assertIn('alt="Elin Nygård"', self.browser.page_source)
        self.assertIn('alt="Anna Andersson"', self.browser.page_source)

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

    def testPrices(self):
        self.assertIn("600", self.browser.page_source)
        self.assertIn("500", self.browser.page_source)
        self.assertIn("200", self.browser.page_source)
        self.assertIn("150", self.browser.page_source)
        self.assertIn("200", self.browser.page_source)
        self.assertIn("560", self.browser.page_source)
        self.assertIn("300", self.browser.page_source)
        self.assertIn("500", self.browser.page_source)

    def testPostalCodePhrase(self):
        self.assertIn("Bring the Salon to Your Home", self.browser.page_source)

    def helperPostalCode(self, postalCodeList, message):
        for currentPostalCode in postalCodeList:
            self.browser.find_element(By.ID, "postalCodeNumber").send_keys(
                currentPostalCode
            )
            time.sleep(0.5)
            self.browser.find_element(By.ID, "submit").click()
            postalOutput = self.browser.find_element(By.ID, "postalCodeCheck")
            self.assertIn(message, postalOutput.text)
            self.browser.get(path.join((getcwd()), "./luleaen.html"))

    def testPostalCodes(self):
        postalCodeListLulea = ["96190", "96191", "96193", "96194"]
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
            postalCodeListLulea,
            "You are within reach. Call us to book a house appointment!",
        )
        self.helperPostalCode(
            notAcceptedPostalCodes,
            "Sorry, we can't offer this service for your location.",
        )
        self.helperPostalCode(nonWorkingPostalCodes, "Not a valid postal code.")

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

        displayed_elements = {
            "IfClosed": self.browser.find_element(By.ID, "displayedIfClosed"),
            "IfOpen": self.browser.find_element(By.ID, "displayedIfOpen"),
            "IfOpenTom": self.browser.find_element(By.ID, "displayedIfOpenTom"),
            "IfOpenToDay": self.browser.find_element(By.ID, "displayedIfOpenToDay"),
            "IfOpenMonday": self.browser.find_element(By.ID, "displayedIfOpenMonday"),
        }

        if (
            expectedResult == "Closed"
            and displayed_elements["IfClosed"].value_of_css_property("display")
            == "block"
            and displayed_elements["IfOpen"].value_of_css_property("display") == "none"
        ):
            if (
                displayed_elements["IfOpenTom"].value_of_css_property("display")
                == "block"
                and displayed_elements["IfOpenToDay"].value_of_css_property("display")
                == "none"
                and displayed_elements["IfOpenMonday"].value_of_css_property("display")
                == "none"
            ):
                self.assertEqual(
                    displayed_elements["IfOpenTom"].text,
                    f"We open tomorrow at: {openTime}",
                )
            elif (
                displayed_elements["IfOpenToDay"].value_of_css_property("display")
                == "block"
                and displayed_elements["IfOpenTom"].value_of_css_property("display")
                == "none"
                and displayed_elements["IfOpenMonday"].value_of_css_property("display")
                == "none"
            ):
                self.assertEqual(
                    displayed_elements["IfOpenToDay"].text,
                    f"We open today at: {openTime}",
                )
            elif (
                displayed_elements["IfOpenMonday"].value_of_css_property("display")
                == "block"
                and displayed_elements["IfOpenToDay"].value_of_css_property("display")
                == "none"
                and displayed_elements["IfOpenTom"].value_of_css_property("display")
                == "none"
            ):
                self.assertEqual(
                    displayed_elements["IfOpenMonday"].text,
                    f"We open on Monday at: {openTime}",
                )
            else:
                self.fail("fel")
        elif (
            expectedResult == "Open"
            and displayed_elements["IfOpen"].value_of_css_property("display") == "block"
            and displayed_elements["IfClosed"].value_of_css_property("display")
            == "none"
            and displayed_elements["IfOpenToDay"].value_of_css_property("display")
            == "none"
            and displayed_elements["IfOpenTom"].value_of_css_property("display")
            == "none"
            and displayed_elements["IfOpenMonday"].value_of_css_property("display")
            == "none"
        ):
            return
        else:
            self.fail("fel2")

    def testAreWeOpen(self):
        # Monday
        self.helperAreWeOpen("2023-10-02T09:59:00", "Closed", "10")
        self.helperAreWeOpen("2023-10-02T10:01:00", "Open", None)
        self.helperAreWeOpen("2023-10-02T16:59:00", "Open", None)
        self.helperAreWeOpen("2023-10-02T17:01:00", "Closed", "10")

        # Tuesday
        self.helperAreWeOpen("2023-10-03T09:59:00", "Closed", "10")
        self.helperAreWeOpen("2023-10-03T10:01:00", "Open", None)
        self.helperAreWeOpen("2023-10-03T15:59:00", "Open", None)
        self.helperAreWeOpen("2023-10-03T16:01:00", "Closed", "10")

        # Wendsday
        self.helperAreWeOpen("2023-10-04T09:59:00", "Closed", "10")
        self.helperAreWeOpen("2023-10-04T10:01:00", "Open", None)
        self.helperAreWeOpen("2023-10-04T14:59:00", "Open", None)
        self.helperAreWeOpen("2023-10-04T15:01:00", "Closed", "10")

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