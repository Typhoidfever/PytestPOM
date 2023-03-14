import time
from random import choice
from string import ascii_letters, digits
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from BaseApp import BasePage


class SiteLocators:
    LOCATOR_COPY_EMAIL_ADDRESS = (By.CSS_SELECTOR, "[id$=pre_copy]")
    LOCATOR_SECOND_EMAIL_IN_LIST = (By.XPATH, "(//div[@class='row no-gutters'])[2]")
    LOCATOR_DELETE_BUTTON = (By.XPATH, "//span[@data-tr='delete']")
    LOCATOR_DELETE_MESSAGE_CONFIRMATION_BUTTON = (By.CSS_SELECTOR, "[id$=confirm_mail]")
    LOCATOR_CREATE_NEW_EMAIL = (By.XPATH, "//span[text()='Написать']")
    LOCATOR_ADDRESS_FIELD = (By.CSS_SELECTOR, "[id$=to]")
    LOCATOR_THEME_FIELD = (By.CSS_SELECTOR, "[id$=subject]")
    LOCATOR_EMAIL_TEXT_FIELD = (By.XPATH, "//div[@id='text']")
    LOCATOR_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[id='submit']")
    LOCATOR_FIRST_EMAIL_IN_LIST = (By.XPATH, "//div[@class='row no-gutters']")


class EmailSendHelper(BasePage):
    message_collection = {}
    summary_message_title = "Summary"
    summary_message_text = ""

    def email_address_copy(self):
        self.find_element(SiteLocators.LOCATOR_COPY_EMAIL_ADDRESS).click()
        time.sleep(5)
        self.find_element(SiteLocators.LOCATOR_CREATE_NEW_EMAIL).click()
        time.sleep(5)
        self.find_element(SiteLocators.LOCATOR_ADDRESS_FIELD).send_keys(Keys.CONTROL, 'v')

    def create_and_send_new_test_email(self):
        topic = ''.join(choice(ascii_letters + digits) for j in range(10))
        text = ''.join(choice(ascii_letters + digits) for k in range(10))
        self.find_element(SiteLocators.LOCATOR_THEME_FIELD).send_keys(topic)
        time.sleep(5)
        self.find_element(SiteLocators.LOCATOR_EMAIL_TEXT_FIELD).send_keys(text)
        time.sleep(5)
        self.find_element(SiteLocators.LOCATOR_SUBMIT_BUTTON).click()
        time.sleep(10)
        self.find_element(SiteLocators.LOCATOR_FIRST_EMAIL_IN_LIST)
        assert True
        self.message_collection.update({topic: text})

    def create_and_send_summary_test_email(self):
        self.find_element(SiteLocators.LOCATOR_CREATE_NEW_EMAIL).click()
        time.sleep(5)
        self.find_element(SiteLocators.LOCATOR_ADDRESS_FIELD).send_keys(Keys.CONTROL, 'v')
        self.find_element(SiteLocators.LOCATOR_THEME_FIELD).send_keys(self.summary_message_title)
        for key in self.message_collection:
            letters_count = 0
            digit_count = 0
            for i in self.message_collection[key]:
                if i.isalpha():
                    letters_count += 1
                elif i.isdigit():
                    digit_count += 1
            self.summary_message_text = f"Received mail on theme {key} with message: "f"{self.message_collection[key]}. It " \
                                        f"consists {letters_count} "f"letters and {digit_count} digits\n"
            self.find_element(SiteLocators.LOCATOR_EMAIL_TEXT_FIELD).send_keys(self.summary_message_text)
        time.sleep(5)
        self.find_element(SiteLocators.LOCATOR_SUBMIT_BUTTON).click()
        time.sleep(10)

    def delete_test_emails(self):
        self.find_element(SiteLocators.LOCATOR_SECOND_EMAIL_IN_LIST).click()
        time.sleep(5)
        self.find_element(SiteLocators.LOCATOR_DELETE_BUTTON).click()
        time.sleep(5)
        self.find_element(SiteLocators.LOCATOR_DELETE_MESSAGE_CONFIRMATION_BUTTON).click()
        time.sleep(5)