from pages.product_page import ProductPage
from pages.compare_page import ComparePage
import pytest
import allure


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.basket
def test_guest_can_add_product_to_basket(browser):
    link = 'https://www.citrus.ua/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_products_page()
    page.go_to_item_page()
    page.add_item_to_basket()
    page.report_allure()
    page.is_right_item_in_basket()


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.compare
@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_can_add_products_for_compare(browser):
    link = 'https://www.citrus.ua/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_products_page()
    page.go_to_item_page()
    compare_page = ComparePage(browser, browser.current_url)
    compare_page.add_to_compare()
    page.go_to_item_page_2()
    compare_page.add_to_compare()
    compare_page.go_to_compare_page()
    page.report_allure()
    compare_page.delete_from_compare()
    compare_page.delete_from_compare()
    compare_page.go_to_main_page()
    compare_page.verify_compare_counter()
    page.report_allure()


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.language
def test_is_right_language_name_of_items(browser):
    link = 'https://www.citrus.ua/uk/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_uk_url()
    page.go_to_products_page()
    page.report_allure()
    page.is_right_language_name_of_items()
