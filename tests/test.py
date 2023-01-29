import random

from core.js_executor import move_to_element
from pages.explicit_wait_page import ExplicitWaitPage


class Test:

    def test_first_example(self, driver):
        url = 'https://demos.telerik.com/aspnet-ajax/ajaxloadingpanel/functionality/explicit-show-hide/defaultcs.aspx'
        page = ExplicitWaitPage(driver, url)
        page.open()

        calendar_days = page.calendar_days()
        day = random.choice(calendar_days)

        move_to_element(driver, day)
        day.click()

        assert day.is_selected()
