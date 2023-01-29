import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    """
    :return: WebDriver
    """
    driver = webdriver.Chrome(executable_path='C:\\Chromedriver\\Chromedriver.exe')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
