from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class DriverFactory:
    @staticmethod
    def get_driver():
        options = webdriver.ChromeOptions()

        #Disabled chrome password manager
        prefs = {"credentials_enable_service" : False,
                 "profile.password_manager_enabled" : False}

        options.add_experimental_option("prefs",prefs)
        options.add_argument("--guest")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

        driver.maximize_window()
        driver.implicitly_wait(5)
        return driver