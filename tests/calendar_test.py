import random

from core.js_executor import move_to_element
from core.urls import first_example_url
from pages.example_page import ExamplePage


class Test:

    def test_first_example(self, driver):
        url = first_example_url
        page = ExamplePage(driver, url)
        page.open()

        calendar_days = page.calendar_days()
        day = random.choice(calendar_days)

        move_to_element(driver, day)
        day.click()

        assert "rcSelected" in day.get_attribute("class")
