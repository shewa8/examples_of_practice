import pytest
from selenium import webdriver
from pages.base_page import LogFile


@pytest.fixture
def browser():
    LogFile.logger.info('Start browser for test..')
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    LogFile.logger.info('Quit browser..')
    browser.quit()
