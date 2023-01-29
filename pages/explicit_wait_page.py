from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ExplicitWaitPage(BasePage):
    _calendar_days = (By.XPATH, ".//table[contains(@class, 'rcMainTable')]//td[@title]")
    _selected_dates = (By.XPATH, ".//fieldset/div/span")

    def calendar_days(self):
        web_elements: [] = self.driver.find_elements(*self._calendar_days)
        return web_elements

    def selected_dates(self):
        web_element = self.driver.find_element(*self._selected_dates)
        return web_element.text.split('\n')
