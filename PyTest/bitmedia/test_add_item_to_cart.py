from pages.product_page import ProductPage
import allure


@allure.severity(allure.severity_level.CRITICAL)
def test_customer_can_add_item_to_cart(browser):
    link = "http://automationpractice.com/index.php"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_item_page()
    page.report_allure()  # allure report
    page.selecting_item_size()  # If need select item size
    page.add_item_to_cart()
    page.registration_new_customer()
    page.shipping_confirm()
    page.is_order_complete()
    page.report_allure()
