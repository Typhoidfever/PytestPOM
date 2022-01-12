import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(scope="session")
def browser():
    driver: WebDriver = webdriver.Chrome(
        executable_path="C://Users//user//PycharmProjects//PytestPOM//chromedriver.exe")
    driver.maximize_window()
    yield driver
    driver.quit()
