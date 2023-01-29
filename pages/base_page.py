from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from core.js_executor import move_to_element


class BasePage:

    def __init__(self, driver: webdriver, url):
        self.driver: webdriver = driver
        self.url: str = url

    def title(self):
        return self.driver.title

    def open(self):
        return self.driver.get(self.url)

    # def find_element(self, by: tuple[By, str]):
    #     element = self.driver.find_element(by)
    #     move_to_element(self.driver, element)
    #     return BaseComponent(element, element._web_element)
    #
    # def find_elements(self):
    #     elements = []

