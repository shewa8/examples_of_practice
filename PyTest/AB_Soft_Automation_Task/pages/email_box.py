from pages.base_page import *
from pages.base_page import LogFile
from pages.locators import EmailAddress
import time


class EmailBox(BasePage):
    def open_message(self):
        LogFile.logger.info('Going to Mail Box')
        element = self.element_to_be_clickable(*EmailAddress.GO_TO_EMAIL_BOX)
        element.click()
        assert element, LogFile.logger.error(f'Element {element} not found')
        time.sleep(Env.vars['wait_time'])

    # Verify mail box link
    def should_be_mbox_url(self):
        assert 'msg' in self.browser.current_url, \
            LogFile.logger.error('"Mail box" isn\'t in current url')
        time.sleep(Env.vars['wait_time'])

    def verify_email_content(self):
        element = self.element_to_be_clickable(*EmailAddress.E_MAIL_CONTENT)
        element.click()
        assert element, LogFile.logger.error('Email message is empty')
