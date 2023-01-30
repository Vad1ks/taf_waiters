import random
import time

from core.js_executor import move_to_element
from core.urls import first_example_url
from pages.explicit_wait_page import ExplicitWaitPage


class Test:

    def test_first_example(self, driver):
        url = first_example_url
        page = ExplicitWaitPage(driver, url)
        page.open()

        for i in range(3):
            calendar_days = page.calendar_days()
            # day = random.choice(calendar_days)
            day_number = random.randint(0, len(calendar_days) - 1)
            day = calendar_days[day_number]

            selected_dates_prev = page.selected_dates()
            selected_dates_prev_len = 0 \
                if 'No Selected Dates to display.' in selected_dates_prev \
                else len(selected_dates_prev)

            move_to_element(driver, day)
            page.wait_until_loader_disappears()
            page.calendar_days()[day_number].click()

            # time.sleep(3)
            # driver.implicitly_wait(3)

            # need to reinit the day web_element
            # to avoid StaleElementExceptionError
            day = page.calendar_days()[day_number]
            assert 'rcSelected' in day.get_attribute("class")
            assert selected_dates_prev_len < len(page.selected_dates())
