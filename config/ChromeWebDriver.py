import os
from selenium import webdriver
from dotenv import load_dotenv
load_dotenv()

class ChromeWebDriver:
    def __init__(self):
        self.driverPath = os.getenv("DRIVER_PATH", "./chromedriver")

    def generateChromeOption(self):
        """
        Setting Up Browser with Arguments
        :return: chrome option object to start the browser
        """
        chrome_options = webdriver.ChromeOptions()
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
        chrome_options.add_argument(f'user-agent={user_agent}')
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--headless")  # Enable this line will run the selenium in background
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--allow-running-insecure-content')
        chrome_options.add_argument('--ignore-certificate-error_checks')
        chrome_options.add_argument('--log-level=OFF')
        chrome_options.add_argument('--lang=en-US,en')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option('prefs', {
            'credentials_enable_service': False,
            'profile': {
                'password_manager_enabled': False
            }
        })

        return chrome_options

    def generateChromeDriver(self):
        """
        Generate chrome driver with chrome options,
        tries to make selenium browser more human oriented
        instead of looks like bot to other web clients
        """
        chrome_options = self.generateChromeOption()

        driver = webdriver.Chrome(executable_path=self.driverPath, options=chrome_options)

        driver.maximize_window()
        return driver

