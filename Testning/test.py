from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import path, getcwd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
from Screenshot import *
import shutil
import os
import time

class TestHemsida(TestCase):
    # settings for the tests
    stangintebrowsern = False # if True, keeps the browser open after the tests are finished
    gomfonstret = False  # shows the browser while the tests run

    # setUpClass runs BEFORE THE FIRST test
    @classmethod
    def setUpClass(cls):
        chr_options = Options()

        if cls.stangintebrowsern:
            chr_options.add_experimental_option("detach", True)

        if cls.gomfonstret:
            chr_options.add_argument("--headless")

        cls.browser = webdriver.Chrome(options=chr_options)

    # tearDownClass runs AFTER THE LAST test
    @classmethod
    def tearDownClass(cls):
        pass

    # setUp runs BEFORE EACH TEST
    def setUp(self):
        pass

    # tearDown runs AFTER EACH TEST
    def tearDown(self):
        # go to a blank page to prevent earlier test from affecting later tests
        self.browser.get('about:blank')


    # the variable is self.browser
    # TESTS BEGIN HERE

    def testPageText(self):
        self.browser.get(path.join(getcwd(), 'index.html'))
        self.assertEqual("Frisör Saxé", self.browser.title)

    def testnavbar(self):
        self.browser.get(path.join(getcwd(), 'index.html'))
        self.assertIn("Hitta oss", self.browser.page_source)
        self.assertIn("Kontakt", self.browser.page_source)
        self.assertIn("Frisör Saxé", self.browser.page_source)

    def testPagedividers(self):
        self.browser.get(path.join(getcwd(), 'index.html'))
        self.assertIn("Välkommen till Frisör Saxé", self.browser.page_source)
        self.assertIn("Priser", self.browser.page_source)
        self.assertIn("Möt vår personal", self.browser.page_source)

    def testdesktop_ss(self):
        
        self.browser.get(path.join(getcwd(), 'index.html'))
        self.browser.save_screenshot("ss_hem.png")
        
        self.browser.get(path.join(getcwd(), 'index.html'))
        self.browser.find_element(By.LINK_TEXT, "Priser").click()
        time.sleep(2)
        self.browser.save_screenshot("ss_priser.png")

        self.browser.get(path.join(getcwd(), 'index.html'))
        self.browser.find_element(By.LINK_TEXT, "Personal").click()
        time.sleep(2)
        self.browser.save_screenshot("ss_personal.png")
        
    def testmobile_ss(self):

        # Set the browser window size to simulate a mobile device (e.g., iPhone X dimensions)
        mobile_emulation = {"deviceName": "iPhone X"}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        # Launch the browser with mobile emulation
        self.browser = webdriver.Chrome(options=chrome_options)

        # Open a website
        self.browser.get(path.join(getcwd(), 'index.html'))  # Replace with the URL you want to visit

        # Continue with your mobile view testing
        self.browser.get(path.join(getcwd(), 'index.html'))
        self.browser.save_screenshot("ss_hem_mobil.png")

    def testPagePictures(self):
        self.browser.get(path.join(getcwd(), 'index.html'))
        
        self.assertIn('alt="orjan"', self.browser.page_source)
        self.assertIn('alt="fredrik"', self.browser.page_source)
        self.assertIn('alt="anna"', self.browser.page_source)
        
        
        
        

# this part makes it so that the tests run if the file runs as a normal python program
if __name__ == '__main__':
    main(verbosity=2)
