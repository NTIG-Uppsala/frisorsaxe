import re
import time
from os import getcwd, path
from unittest import TestCase, main

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestHomepageNoScript(TestCase):
    doNotCloseBrowser = False
    hideWindow = True

    # Before the first test
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
        self.browser.get(path.join(getcwd(), "./kirunasv.html"))

    # After each test
    def tearDown(self):
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
        self.browser.get(path.join(getcwd(), "./kirunasv.html"))

    # After each test
    def tearDown(self):
        self.browser.get("about:blank")

    def testTitle(self):
        self.assertEqual("Frisör Saxé", self.browser.title)

    def testMap(self):
        self.browser.find_element(By.ID, "hittaoss")
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
        self.assertIn("E‑post", self.browser.page_source)
        self.assertIn("0630‑555‑555", self.browser.page_source)
        self.assertIn("saxefrisor@gmail.com", self.browser.page_source)

    def testOpeningHours(self):
        self.assertIn("Öppettider", self.browser.page_source)
        self.assertIn("Mån", self.browser.page_source)
        self.assertIn("Fre", self.browser.page_source)
        self.assertIn("Lördag", self.browser.page_source)
        self.assertIn("Söndag", self.browser.page_source)
        self.assertIn("Stängt", self.browser.page_source)

    def testInfo(self):
        self.assertIn("Gränsen för långt hår går vid 20 cm", self.browser.page_source)
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
        self.assertIn("Skägg", self.browser.page_source)

    def testNavbar(self):
        nabBrand = self.browser.find_element(By.ID, "centerText")
        self.assertIn("Frisör&nbsp;Saxé", nabBrand.get_attribute("innerHTML"))
        element = self.browser.find_element(By.CLASS_NAME, "navbar-nav")
        self.assertIn("Boka tid", element.get_attribute("innerHTML"))
        self.assertIn("Öppettider", element.get_attribute("innerHTML"))
        self.assertIn("Priser", element.get_attribute("innerHTML"))
        self.assertIn("Personal", element.get_attribute("innerHTML"))
        self.assertIn("Hitta oss", element.get_attribute("innerHTML"))

    def testEmployeeHeader(self):
        self.assertIn("Möt vår personal", self.browser.page_source)

    def testEmployeePictures(self):
        self.assertIn('alt="Örjan Johansson"', self.browser.page_source)
        self.assertIn('alt="Fredrik Örtqvist"', self.browser.page_source)
        self.assertIn('alt="Anna Pettersson"', self.browser.page_source)

    def testEmployeeJobs(self):
        self.assertIn("Hårstylist", self.browser.page_source)
        self.assertIn("Barberare", self.browser.page_source)

    def testAddress(self):
        self.assertIn("Adress", self.browser.page_source)

    def testPrices(self):
        self.assertIn("600", self.browser.page_source)
        self.assertIn("500", self.browser.page_source)
        self.assertIn("200", self.browser.page_source)
        self.assertIn("150", self.browser.page_source)
        self.assertIn("200", self.browser.page_source)
        self.assertIn("560", self.browser.page_source)
        self.assertIn("300", self.browser.page_source)
        self.assertIn("500", self.browser.page_source)

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
        # Checks if the element is displayed
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
        self.assertIn("Proffsiga klippningar hemma", self.browser.page_source)

    def helperPostalCode(self, postalcodeList, message):
        for currentPostalCode in postalcodeList:
            self.browser.find_element(By.ID, "postalCodeNumber").send_keys(
                currentPostalCode
            )
            time.sleep(0.5)
            self.browser.find_element(By.ID, "submit").click()
            postalOutput = self.browser.find_element(By.ID, "postalCodeCheck")
            self.assertIn(message, postalOutput.text)
            self.browser.get(path.join((getcwd()), "./kirunasv.html"))

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
            postalCodeListKiruna, "Vi kör ut till dig. Ring oss för att boka tid!"
        )
        self.helperPostalCode(
            notAcceptedPostalCodes,
            "Vi kan tyvärr inte erbjuda denna service för detta postnummer.",
        )
        self.helperPostalCode(nonWorkingPostalCodes, "Inte ett riktigt postnummer.")

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
            "IfOpenMonday": self.browser.find_element(By.ID, "displayedIfSaturdayAfterHours"),
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
                    f"Vi öppnar imorgon kl. {openTime}",
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
                    f"Vi öppnar idag kl. {openTime}",
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
                    f"Vi öppnar på måndag kl. {openTime}",
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
