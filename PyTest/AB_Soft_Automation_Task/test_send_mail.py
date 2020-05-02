from helpers.send_mail import *
from pages.email_box import EmailBox
import allure


@allure.severity(allure.severity_level.NORMAL)
def test_sent_email(browser):
    link = 'https://getnada.com/'
    page = CopyEmailAddress(browser, link)
    page.open()
    page.send_message_to_email_address()
    mail_box = EmailBox(browser, browser.current_url)
    page.report_allure()
    mail_box.open_message()
    mail_box.should_be_mbox_url()
    mail_box.verify_email_content()
    page.report_allure()
