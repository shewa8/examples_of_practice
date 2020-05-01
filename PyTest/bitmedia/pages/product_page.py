from pages.base_page import BasePage
from pages.base_page import LogFile
from pages.base_page import Env
from pages.locators import ProductPageLocatots
from pages.locators import RegNewCustomer
from pages.locators import ShippingAgree
from selenium.webdriver.support.ui import Select
import time


class ProductPage(BasePage):
    def go_to_item_page(self):
        LogFile.logger.info('Going to item page.')
        element = self.browser.find_element(*ProductPageLocatots.ITEM_PAGE)
        element.click()

    def selecting_item_size(self):
        element = Select(self.element_to_be_present(*ProductPageLocatots.SELECT_SIZE))
        element.select_by_value('2')

    def add_item_to_cart(self):
        element = self.element_to_be_present(*ProductPageLocatots.NAME_OF_PRODUCT)
        name_of_item = element.text
        element = self.element_to_be_clickable(*ProductPageLocatots.ADD_CART)
        element.click()
        assert element, LogFile.logger.error(f'Element "{element}" not found.')
        LogFile.logger.info(f'Item "{name_of_item}" is successfully added to cart.')
        element = self.element_to_be_clickable(*ProductPageLocatots.CHECKOUT_BTN)
        element.click()
        element = self.element_to_be_present(*ProductPageLocatots.IN_STOCK)
        is_item_in_stock = element.text
        assert "In stock" == is_item_in_stock, \
            LogFile.logger.error(f'Item should be "In stock", but it is {is_item_in_stock}.')
        element = self.browser.find_element(*ProductPageLocatots.CHECKOUT_BTN_2)
        time.sleep(Env.vars['wait_time'])

        # JS script - anyway button will be pressed even if some windows block it
        self.browser.execute_script('arguments[0].click();', element)

    def registration_new_customer(self):
        LogFile.logger.info('Registration new customer.')
        element = self.element_to_be_present(*RegNewCustomer.CREATE_ACC)

        # Generates different email
        element.send_keys(str(time.time()) + '@fakemail.org')
        element = self.browser.find_element(*RegNewCustomer.CREATE_SUBMIT_BTN)
        element.click()

        # Fill up ONLY required field
        element = self.element_to_be_present(*RegNewCustomer.FIRST_NAME)
        element.send_keys('Vladyslav')
        element = self.browser.find_element(*RegNewCustomer.LAST_NAME)
        element.send_keys('Shevchenko')
        element = self.browser.find_element(*RegNewCustomer.PASSWD)
        element.send_keys('46464rte.1!@fdfs')
        element = self.browser.find_element(*RegNewCustomer.ADRESS)
        element.send_keys('Odessa')
        element = self.browser.find_element(*RegNewCustomer.CITY)
        element.send_keys('Odessa')
        element = Select(self.browser.find_element(*RegNewCustomer.STATE))
        element.select_by_value('2')
        element = self.browser.find_element(*RegNewCustomer.POSTCODE)
        element.send_keys('65000')
        element = self.browser.find_element(*RegNewCustomer.PHONE_NUMBER)
        element.send_keys('1234567890')
        element = self.browser.find_element(*RegNewCustomer.SUMBIT_BTN)
        element.click()
        element = self.browser.find_element(*RegNewCustomer.CHECKOUT_BTN)
        element.click()
        time.sleep(Env.vars['wait_time'])
        LogFile.logger.info('Registration is complete.')

    def shipping_confirm(self):
        LogFile.logger.info('Confirm shipping')
        element = self.element_to_be_present(*ShippingAgree.CHECK_BOX_AGREE)
        element.click()
        element = self.browser.find_element(*ShippingAgree.CHECKOUT_BTN)
        element.click()
        LogFile.logger.info('Selecting payment method.')
        element = self.browser.find_element(*ShippingAgree.PAYMENT)
        element.click()
        time.sleep(Env.vars['wait_time'])
        element = self.element_to_be_present(*ShippingAgree.CONFIRM_ORDER)
        self.browser.execute_script('arguments[0].click();', element)

    def is_order_complete(self):
        element = self.element_to_be_present(*ProductPageLocatots.ORDER_COMPLETE)
        order_complete = element.text
        LogFile.logger.info(f'Order successfully complete.')
        assert 'Your order on My Store is complete.' == order_complete, \
            LogFile.logger.error(f'Order isn\'t complete.')
