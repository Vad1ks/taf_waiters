from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_wait(driver):
    driver.get("https://gokcecapital.com/free-land")

    WebDriverWait(driver, timeout=15, poll_frequency=2,
                  ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException]) \
        .until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="bottom-box-text-p"]')))
    text = driver.find_element(By.XPATH, '//*[@id="bottom-box-text-p"]/span/b').text
    print("text:", text)
    assert '$100' in text
