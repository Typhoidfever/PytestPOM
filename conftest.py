import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(scope="function")
def browser():
    driver: WebDriver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
