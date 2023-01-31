import random
import time

from core.js_executor import move_to_element
from core.urls import first_example_url
from pages.example_page import ExamplePage


def remove_zero_before_day_number(date: str):
    month = date.split(',')[1].split(' ')
    month[2] = month[2][1] if month[2][0] == '0' else month[2]
    date = date.split(',')
    date[1] = ' '.join(month)
    return ','.join(date)


class Test:

    def test_first_example(self, driver):
        checked_days = []
        url = first_example_url
        page = ExamplePage(driver, url)
        page.open()

        for i in range(3):
            calendar_days = page.calendar_days()
            day_number = random.randint(0, len(calendar_days) - 1)

            while day_number in checked_days:
                day_number = random.randint(0, len(calendar_days) - 1)

            checked_days.append(day_number)
            day = calendar_days[day_number]

            selected_dates_prev = page.selected_dates()
            selected_dates_prev_len = 0 \
                if 'No Selected Dates to display.' in selected_dates_prev \
                else len(selected_dates_prev)

            move_to_element(driver, day)
            page.calendar_days()[day_number].click()
            page.wait_until_loader_disappears(timeout=3)

            expected_day_text = remove_zero_before_day_number(page.calendar_days()[day_number].
                                                              get_attribute("title"))
            assert selected_dates_prev_len < len(page.selected_dates())
            assert expected_day_text in page.selected_dates()
