from helpers.send_mail import *
from pages.email_box import EmailBox
import allure


@allure.severity(allure.severity_level.NORMAL)
def test_sent_email(browser):
    link = 'https://getnada.com/'
    page = CopyEmailAddress(browser, link)
    page.open()
    page.send_message_to_email_address()
