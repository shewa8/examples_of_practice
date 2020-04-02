from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

link = 'https://www.google.com/'


@given('the Google main page is opened')
def step_impl(context):
    context.browser.get(link)


@when('the user searches for "{phrase}"')
def step_impl(context, phrase):
    search_field = context.browser.find_element(By.NAME, 'q')
    search_field.send_keys(phrase + Keys.RETURN)


@then('results are shown for "{phrase}"')
def step_impl(context, phrase):
    search_result = context.browser.find_element(By.ID, 'search')
    assert len(search_result.find_elements(By.XPATH, '//div')) > 0
    search_input = context.browser.find_element(By.NAME, 'q')
    assert search_input.get_attribute('value') == phrase
