from selenium.webdriver.chrome import webdriver


class BasePage:

    def __init__(self, driver: webdriver, url):
        self.driver: webdriver = driver
        self.url: str = url

    def title(self):
        return self.driver.title

    def open(self):
        return self.driver.get(self.url)
