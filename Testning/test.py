from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import path, getcwd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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


# this part makes it so that the tests run if the file runs as a normal python program
if __name__ == '__main__':
    main(verbosity=2)
