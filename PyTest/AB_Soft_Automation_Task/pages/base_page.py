from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from allure_commons.types import AttachmentType
import allure
import logging
import os


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    # Wait for present of element (Explicit Waits)
    def element_to_be_present(self, how, what, timeout=30):
        try:
            driver_wait = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return driver_wait

    # Wait for element to be clickable (Explicit Waits)
    def element_to_be_clickable(self, how, what, timeout=30):
        try:
            driver_wait = WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return driver_wait

    def report_allure(self):
        allure.attach(
            self.browser.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=AttachmentType.PNG
        )


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


class Env:
    vars = {
        'wait_time': 1,
        'verify_time': 5
    }
