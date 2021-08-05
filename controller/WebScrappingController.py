import datetime
import logging

from model.Product import Product
from service.ValidationService import ValidationService
from service.WebService import WebService


class WebScrappingController:
    def __init__(self):
        self.webService = WebService()
        self.productModel = None

    def runWebBrowser(self):
        '''
         Setup the browser with additional header and other content
         and run the browser for scrapping
        '''
        self.webService.setupWebDriver()

    def getScrapedProductList(self, url, xpath):
        """
        :param url: The website which need to scrapped
        :param xpath: The xpath of the element of critical product
        :return: the webelement of the xpath
        """
        self.webService.goToUrl(url)
        container = self.webService.findElementsByXpath(xpath)
        return container

    def extractProductandUnitFromList(self, productWebElementList):
        """
        :param productWebElementList: list of spans of webElement
        :return: product after extract the data and makes a list of data
        """
        products = []
        try:
            for productSpan in productWebElementList:
                products.append(self.extractNameUnitFromWebElement(productSpan))
        except Exception as e:
            logging.exception(f" can not extract product from list `")

        return products

    def extractNameUnitFromWebElement(self, productSpanElement):
        """
        :param productSpanElement: WebElement which contain product name and unit in span tag
        :return: formate the name and unit and return a single dict of the product
        """
        try:
            productName = self.webService.getContentFromXPATH(productSpanElement, 'span[contains(@class, "bold")]')
            productUnit = self.webService.getContentFromXPATH(
                productSpanElement, 'span[contains(@class, "line-item-bold")]')

            '''
             To get the amount and unit seperately , unit string is splatted .
             after pop the amount, rest elements is joined as a string again
             to check multiple space issue 
            '''
            productUnitList = productUnit.split()

            amount = productUnitList.pop(0).replace(',', '')
            unit = ' '.join([str(x).strip() for x in productUnitList])

            time = datetime.datetime.now()

            return {"product": productName.replace(':', ''), "amount": int(amount), "unit": unit, "created_at": time}

        except Exception as e:
            logging.exception(f" can not extract product from Element `")
            return {}

    def scrapedAndStoreProductData(self, url, xpath):
        """
        This is the mail method that combine all method in a single method and execute the task
        :param url: the url of the scraped site
        :param xpath: xpath of where the critical product element available
        :return: after extract the data and validating, return the mongodb insertion instance
        """
        try:
            productWebElementList = self.getScrapedProductList(url, xpath)

            productData = self.extractProductandUnitFromList(productWebElementList)

            ValidationService().productValidate(productData)

            return Product().insertManyProduct(productData)

        except Exception as e:
            logging.exception(f" can not extract product from Element `")
            raise e

    def closeBroswer(self):
        self.webService.closeSession()
