from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class ExamplePage(BasePage):
    _calendar_days = (By.XPATH, ".//table[contains(@class, 'rcMainTable')]//td[@title]")
    _selected_dates = (By.XPATH, ".//fieldset/div/span")
    _loader = (By.XPATH, "//div[@class='raDiv']")
    _clear_button = (By.XPATH, "//button[contains(@class, 'clearBtn')]")

    def calendar_days(self):
        ignored_exceptions = (StaleElementReferenceException,)
        web_elements = WebDriverWait(self.driver, timeout=10, ignored_exceptions=ignored_exceptions) \
            .until(
            expected_conditions.presence_of_all_elements_located(self._calendar_days)
        )
        return web_elements

    def selected_dates(self):
        web_element = self.driver.find_element(*self._selected_dates)
        return web_element.text.split('\n')

    def wait_until_loader_disappears(self, timeout=10):
        #ignored_exceptions = (StaleElementReferenceException, NoSuchElementException)
        WebDriverWait(self.driver, timeout=timeout) \
            .until_not(
            expected_conditions.visibility_of_element_located(self._loader)
        )

    def clear_button(self):
        return self.driver.find_element(*self._clear_button)
