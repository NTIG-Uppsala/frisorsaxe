import time
from os import getcwd, path
from unittest import TestCase, main

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestHemsida(TestCase):
    # Inställningar för testerna
    stangintebrowsern = (
        False  # Om True, håller webbläsaren öppen efter att testerna är klara
    )
    gomfonstret = False  # Visar webbläsaren medan testerna körs

    # setUpClass körs FÖRE DET FÖRSTA testet
    @classmethod
    def setUpClass(cls):
        chr_options = Options()

        if cls.stangintebrowsern:
            chr_options.add_experimental_option("detach", True)

        if cls.gomfonstret:
            chr_options.add_argument("--headless")

        cls.browser = webdriver.Chrome(options=chr_options)

    # tearDownClass körs EFTER DET SISTA testet
    @classmethod
    def tearDownClass(cls):
        pass

    # setUp körs FÖRE VARJE TEST
    def setUp(self):
        pass

    # tear_down körs EFTER VARJE TEST
    def tear_down(self):
        # Gå till en tom sida för att förhindra att tidigare tester påverkar senare tester
        self.browser.get("about:blank")

    # Variabeln för Selenium är self.browser
    # TESTER BÖRJAR HÄR

    def test_ID(self):
        # Besök webbsidan och kontrollera att sidtiteln är "Frisör Saxé"
        self.browser.get(path.join(getcwd(), "index.html"))
        element = 0
        # Find the element by its ID

        element = self.browser.find_element(By.ID, "bokatid")

        # If the element is found, you can perform actions on it
        # For example, you can print its text
        print("aaaahg")
        print(element)

    def test_title(self):
        # Besök webbsidan och kontrollera att sidtiteln är "Frisör Saxé"
        self.browser.get(path.join(getcwd(), "index.html"))
        self.assertEqual("Frisör Saxé", self.browser.title)

    def test_map(self):
        # Besök webbsidan och kontrollera om texten "map" finns på sidan
        self.browser.get(path.join(getcwd(), "index.html"))
        self.assertIn("karta", self.browser.page_source)

    def test_first_page_text(self):
        # Besök webbsidan och kontrollera om olika textfragment finns på sidan
        self.browser.get(path.join(getcwd(), "index.html"))
        self.assertIn("Telefon", self.browser.page_source)
        self.assertIn("Mail", self.browser.page_source)
        self.assertIn("Lördag", self.browser.page_source)
        self.assertIn("Fjällgatan", self.browser.page_source)
        self.assertIn("Öppettider", self.browser.page_source)
        self.assertIn("Kontakta", self.browser.page_source)
        self.assertIn("Hitta", self.browser.page_source)

    def test_second_page_text(self):
        # Besök webbsidan och kontrollera om olika textfragment finns på sidan
        self.browser.get(path.join(getcwd(), "index.html"))
        self.assertIn("Klippning", self.browser.page_source)
        self.assertIn("Långt", self.browser.page_source)
        self.assertIn("Övrigt", self.browser.page_source)
        self.assertIn("Färgning", self.browser.page_source)

    def test_navbar(self):
        # Besök webbsidan och kontrollera om olika länkar finns i navigationsmenyn
        self.browser.get(path.join(getcwd(), "index.html"))
        self.assertIn("Hitta oss", self.browser.page_source)
        self.assertIn("Frisör Saxé", self.browser.page_source)

    def test_page_dividers(self):
        # Besök webbsidan och kontrollera om olika avsnittsindelningar finns
        self.browser.get(path.join(getcwd(), "index.html"))
        self.assertIn("Lyx och skönhet", self.browser.page_source)
        self.assertIn("Priser", self.browser.page_source)
        self.assertIn("Möt vår personal", self.browser.page_source)

    def test_desktop_ss(self):
        # Besök webbsidan och ta skärmdumpar på olika delar
        self.browser.get(path.join(getcwd(), "index.html"))
        time.sleep(2)
        self.browser.save_screenshot("ss_hem.png")

        self.browser.get(path.join(getcwd(), "index.html"))
        self.browser.find_element(By.LINK_TEXT, "Priser").click()
        time.sleep(2)
        self.browser.save_screenshot("ss_priser.png")

        self.browser.get(path.join(getcwd(), "index.html"))
        self.browser.find_element(By.LINK_TEXT, "Personal").click()
        time.sleep(2)
        self.browser.save_screenshot("ss_personal.png")

        self.browser.get(path.join(getcwd(), "index.html"))
        self.browser.find_element(By.LINK_TEXT, "Hitta oss").click()
        time.sleep(2)
        self.browser.save_screenshot("ss_karta.png")

    def testmobile_ss(self):
        # Ställ in webbläsarfönstrets storlek för att simulera en mobil enhet (t.ex. iPhone X-dimensioner)
        mobile_emulation = {"deviceName": "iPhone X"}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        # Starta webbläsaren med mobilsimulering
        self.browser = webdriver.Chrome(options=chrome_options)

        # Öppna en webbplats
        self.browser.get(path.join(getcwd(), "index.html"))
        self.browser.save_screenshot("ss_hem_mobil.png")

    def test_page_pictures(self):
        # Besök webbsidan och kontrollera om olika bilder finns
        self.browser.get(path.join(getcwd(), "index.html"))

        self.assertIn('alt="orjan"', self.browser.page_source)
        self.assertIn('alt="fredrik"', self.browser.page_source)
        self.assertIn('alt="anna"', self.browser.page_source)


# Denna del gör att testerna körs om filen körs som ett vanligt Python-program
if __name__ == "__main__":
    main(verbosity=2)
