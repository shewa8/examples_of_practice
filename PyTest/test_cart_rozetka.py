# Expected result: 2 item will be add to cart


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "https://rozetka.com.ua/"


def test_add_item_to_cart(browser, timeout=10):
    # Open link, send request for search of item
    browser.get(link)
    search_field = browser.find_element(By.CSS_SELECTOR, ".search-form__input.ng-untouched")
    search_field.send_keys("Изучаем Python")
    search_button = WebDriverWait(browser, timeout).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".button.search-form__submit")))
    search_button.click()

    # Open page with first item from catalog
    searched_item = WebDriverWait(browser, timeout).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "li.catalog-grid__cell:first-child")))
    searched_item.click()

    # Add item to cart; Anyway button will be pressed even if some windows block it
    add_to_cart_button = WebDriverWait(browser, timeout).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.buy-button")))
    browser.execute_script("arguments[0].click();", add_to_cart_button)

    # Add to cart second item
    add_second_item = WebDriverWait(browser, timeout).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-modal__calc-button:last-child")))
    add_second_item.click()
    time.sleep(5)

    # Checking the presence of 2 items in cart by the sum of their prices
    price_of_one_item = browser.find_element(By.CSS_SELECTOR, ".cart-modal__coast:first-child")
    price_of_one_item_txt = price_of_one_item.text
    price_of_two_item = browser.find_element(By.CSS_SELECTOR, ".cart-modal__coast:last-child")
    price_of_two_item_txt = price_of_two_item.text
    assert price_of_one_item_txt != price_of_two_item_txt, \
        'Looks like that only one item added to cart'
