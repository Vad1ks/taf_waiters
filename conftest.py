import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    """
    :return: WebDriver
    """
    driver = webdriver.Chrome(executable_path='C:\\Chromedriver\\Chromedriver.exe')
    driver.maximize_window()
    yield driver
    driver.quit()
