from selenium.common.exceptions import NoSuchElementException
from pages.locators import BasePageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import allure
from allure_commons.types import AttachmentType
import os


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_main_page(self):
        language_link = self.browser.find_element(*BasePageLocators.GO_TO_MAIN_PAGE)
        language_link.click()

    def go_to_change_language(self):
        language_link = self.browser.find_element(*BasePageLocators.LANGUAGE_LINK)
        language_link.click()

    def should_be_language_link(self):
        assert self.is_element_present(*BasePageLocators.LANGUAGE_LINK), \
            LogFile.logger.error('"Language" link is not presented')

    def should_be_uk_url(self):
        assert 'uk' in self.browser.current_url, \
            LogFile.logger.error('"Ukrainian" not in current url')

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def element_to_be_clickable(self, how, what, timeout=10):
        try:
            driver_wait = WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return driver_wait

    def element_to_be_present(self, how, what, timeout=10):
        try:
            driver_wait = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return driver_wait

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def report_allure(self):
        allure.attach(
            self.browser.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=AttachmentType.PNG
        )


class Env:
    vars = {
        'wait_time': 1,
        'verify_time': 5
    }


class LogFile:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    log_directory = "reports/logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
        file_handler = logging.FileHandler('reports/logs/log_file.log')
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
