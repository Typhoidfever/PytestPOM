import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def browser():
    chrome_options = Options()
    chrome_options.add_extension('C:\\Users\\user\\PycharmProjects\\PytestPOM\\extension_3_16_2_0.crx')
    driver: WebDriver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()
