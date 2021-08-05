import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.ChromeWebDriver import ChromeWebDriver


class WebService:
    def __init__(self):
        self.chromeWebDriver = ChromeWebDriver()
        self.driver = None

    def setupWebDriver(self):
        """
        Generate chrome driver
        """
        self.driver = self.chromeWebDriver.generateChromeDriver()

    def goToUrl(self, url):
        """
        Goes to given url and wait 2 seconds to load the site
        :param url: the website url where scrapper needs to go
        """
        self.driver.get(url)
        time.sleep(2)

    def waitUntilFindElementByXpath(self, xpath):
        """
        The webdriver will wait for 10 second for the element to be existed
        if webdriver can not find the element within 10 second , its rise exception
        :param xpath:
        :return: Webelement of the xpath
        """
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
        except Exception as e:
            logging.exception(f" can not find the XPATH `{xpath} `")
            return None

    def findElementByXpath(self, xpath):
        """
        find element by xpath and return of this web element
        """
        try:
            time.sleep(3)
            return self.driver.find_element_by_xpath(xpath)
        except Exception as e:
            logging.exception(f" can not find the XPATH `{xpath} `")
            return None

    def findElementsByXpath(self, xpath):
        """
        find the element by xpath and return the list
        """
        try:
            time.sleep(3)
            return self.driver.find_elements_by_xpath(xpath)
        except Exception as e:
            logging.exception(f" can not find the XPATH `{xpath} `")
            return None

    def findElementContainerByTag(self, container, tag):
        """
        find and return the tag exist in this webelement container
        :param container: a web element
        :param tag: string tag like "span"
        :return: another web element
        """
        try:
            return container.findElements(By.TAG_NAME, tag)
        except Exception as e:
            logging.exception(f" can not find the tag `{tag}` ")
            return None

    def getContentFromXPATH(self, container, xpath):
        """
        find the xpath exist in this web element container
        and return its inner html
         :param container: a web element
        :param xpath: string xpath
        :return: string inner html
        """
        try:
            element = container.find_element_by_xpath(xpath)

            return element.get_attribute('innerHTML').strip()

        except Exception as e:
            logging.exception(f" can not get the content from xpath : `{xpath}` ")
            return None

    def closeSession(self):
        """
        close session and browser
        """
        self.__exit__()

    def __exit__(self):
        try:
            if self.driver is not None:
                self.driver.close()
                self.driver.quit()
        except Exception as e:
            print(str(e))
            pass
