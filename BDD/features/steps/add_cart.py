from behave import *
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

use_step_matcher("re")
driver_wait = 10


@when("I opened (?P<link>.+) using (?P<browser>.+)")
def step_impl(context, link, browser):
    """
    :type context: behave.runner.Context
    :type link: str
    :type browser: str
    """
    print(f'Opening {link} in {browser}')
    context.browser.get(link)
    attach(
        context.browser.get_screenshot_as_png(),
        name="screenshot",
        attachment_type=AttachmentType.PNG
    )


@when("I fill up (?P<item_name>.+) into search (?P<field>.+) and press on (?P<item>.+)")
def step_impl(context, item_name, field, item):
    """
    :type context: behave.runner.Context
    :type item_name: str
    :type field: str
    :type item: str
    """
    element = context.browser.find_element(By.CSS_SELECTOR, field)
    assert element, 'Element not found'
    element.send_keys(item_name + Keys.RETURN)
    element = WebDriverWait(context.browser, driver_wait).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, item))
    )
    assert element, 'Element not found'
    # Added method 'execute_script' for executing JS
    # Anyway button will be pressed even if some windows block it
    context.browser.execute_script("arguments[0].click();", element)
    print(f'Successfully filled up {field} by {item_name} and selected {item}')


@when("I open page with (?P<item_name>.+) and press (?P<buy_button>.+)")
def step_impl(context, item_name, buy_button):
    """
    :type context: behave.runner.Context
    :type item_name: str
    :type buy_button: str
    """
    element = WebDriverWait(context.browser, driver_wait).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, buy_button))
    )
    assert element, 'Element not found'
    context.browser.execute_script("arguments[0].click();", element)
    print(f'Successfully opened page with {item_name} and pressed {buy_button}')


@then("I verify the availability of the (?P<item_name>.+) in the (?P<cart>.+)")
def step_impl(context, item_name, cart):
    """
    :type context: behave.runner.Context
    :type item_name: str
    :type cart: str
    """
    element = context.browser.find_elements(By.CSS_SELECTOR, cart)
    assert element, 'Element not found'
    attach(
        context.browser.get_screenshot_as_png(),
        name="screenshot",
        attachment_type=AttachmentType.PNG
    )
    assert len(element) == 1, f'{item_name} not added to cart'
    print(f'Successfully verified the availability of the {item_name} in the {cart}')
