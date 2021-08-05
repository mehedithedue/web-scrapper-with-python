import logging
import os
import time

from controller.WebScrappingController import WebScrappingController

logging.basicConfig(filename='log/scrapper.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(name)s : %(message)s')

'''
-----------------------------------------------------
To run this scrapper please give the command ( example )
python index.py 
-----------------------------------------------------
'''

if __name__ == "__main__":

    '''
    Start the web browser for scrapping
    '''
    webScrapper = WebScrappingController()
    webScrapper.runWebBrowser()

    '''
    while true to continuous run the script
    '''
    while True:

        try:

            url = os.getenv("WEB_URL", 'https://www.google.com')

            xpath = '//div[@class="critical-product-marquee-container"]//div[@class="marquee-text-text"][1]/span/span'

            '''
             Go to Url and search for given xpath, 
             find the elements, extracted the value and 
             store in mongo database
            '''
            webScrapper.scrapedAndStoreProductData(url, xpath)

            '''
             Make sure the scrapping will continue every 5 minute delay 
             (value is  in env so its configurable)
             otherwise the its cause additional overload to scrapped website
             also current system have additional load
            '''
            time.sleep(os.getenv("SCRAPPING_DELAY_SECOND", 300))


        except Exception as e:
            logging.exception("Exception : ")
            webScrapper.closeBroswer()
            '''
             Raise the exception because its main thread 
            '''
            raise e