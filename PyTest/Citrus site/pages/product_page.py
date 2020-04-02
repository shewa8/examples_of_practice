from pages.base_page import BasePage
from pages.base_page import Env
from pages.base_page import LogFile
from pages.locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def go_to_products_page(self):
        LogFile.logger.info('Guest going to page with products')
        product_page = self.element_to_be_clickable(*ProductPageLocators.PRODUCT_LINK)
        assert product_page, LogFile.logger.error(f'Element {ProductPageLocators.PRODUCT_LINK} not found')
        product_page.click()
        LogFile.logger.info(f'Element {ProductPageLocators.PRODUCT_LINK} successfully found and clicked')
        time.sleep(Env.vars['wait_time'])
        is_second_page = self.is_element_present(*ProductPageLocators.PRODUCT_LINK_2)
        if is_second_page is True:
            element = self.element_to_be_clickable(*ProductPageLocators.PRODUCT_LINK_2)
            assert element, LogFile.logger.error(f'Element {ProductPageLocators.PRODUCT_LINK_2} not found')
            element.click()
            LogFile.logger.info(f'Element {ProductPageLocators.PRODUCT_LINK_2} successfully found and clicked')
            time.sleep(Env.vars['wait_time'])
            is_third_page = self.is_element_present(*ProductPageLocators.PRODUCT_LINK_3)
            if is_third_page is True:
                element = self.element_to_be_clickable(*ProductPageLocators.PRODUCT_LINK_3)
                assert element, LogFile.logger.error(f'Element {ProductPageLocators.PRODUCT_LINK_3} not found')
                element.click()
                LogFile.logger.info(f'Element {ProductPageLocators.PRODUCT_LINK_3} successfully found and clicked')
                time.sleep(Env.vars['wait_time'])

    def go_to_item_page(self):
        LogFile.logger.info('Guest going to open page with some product')
        item_page = self.element_to_be_clickable(*ProductPageLocators.ITEM_PAGE_1)
        assert item_page, LogFile.logger.error(f'Element {ProductPageLocators.ITEM_PAGE_1} not found')
        item_page.click()
        LogFile.logger.info(f'Element {ProductPageLocators.ITEM_PAGE_1} successfully found and clicked')
        time.sleep(Env.vars['wait_time'])

    def go_to_item_page_2(self):
        LogFile.logger.info('Guest going to open page with another product')
        self.browser.execute_script("window.history.go(-1)")  # go to backpage
        item_page = self.element_to_be_clickable(*ProductPageLocators.ITEM_PAGE_2)
        assert item_page, LogFile.logger.error(f'Element {ProductPageLocators.ITEM_PAGE_2} not found')
        item_page.click()
        LogFile.logger.info(f'Element {ProductPageLocators.ITEM_PAGE_2} successfully found and clicked')
        time.sleep(Env.vars['wait_time'])

    def add_item_to_basket(self):
        LogFile.logger.info('Guest going to add product to basket')
        add_to_basket = self.element_to_be_clickable(*ProductPageLocators.ADD_TO_BASKET)
        assert add_to_basket, LogFile.logger.error(f'Element {ProductPageLocators.ADD_TO_BASKET} not found')
        add_to_basket.click()
        LogFile.logger.info(f'Element {ProductPageLocators.ADD_TO_BASKET} successfully found and clicked')
        time.sleep(Env.vars['wait_time'])

    def is_right_item_in_basket(self):
        LogFile.logger.info('Guest going to verify is right product in basket')
        element = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert element, LogFile.logger.error(f'Element {ProductPageLocators.PRODUCT_NAME} not found')
        product_name = element.text
        element = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        assert element, LogFile.logger.error(f'Element {ProductPageLocators.PRODUCT_NAME_IN_BASKET} not found')
        product_in_basket = element.text
        assert product_name == product_in_basket, \
            f'Added {product_in_basket}, but should be {product_name}'
        LogFile.logger.info(f'Product {product_in_basket} successfully added to basket')

    def is_right_language_name_of_items(self):
        LogFile.logger.info('I\'m going to verify that all product names are translated into Ukrainian')
        skip_button = self.browser.find_element(*ProductPageLocators.SKIP_BUTTON)
        assert skip_button, LogFile.logger.error(f'Element {ProductPageLocators.SKIP_BUTTON} not found')
        skip_button_number = int(skip_button.text)
        count = 0
        while count <= skip_button_number:
            element = self.is_element_present(*ProductPageLocators.CATALOG_CARD)
            if element is True:
                element = self.element_to_be_clickable(*ProductPageLocators.CATALOG_CARD)
                assert skip_button, LogFile.logger.error(f'Element {ProductPageLocators.CATALOG_CARD} not found')
                element.click()
                time.sleep(Env.vars['wait_time'])
            count += 1
        all_item_list = self.browser.find_elements(*ProductPageLocators.LIST_OF_ITEMS)
        assert skip_button, LogFile.logger.error(f'Elements {ProductPageLocators.LIST_OF_ITEMS} not found')
        for name in all_item_list:
            item_title = name.get_attribute('title')
            names_that_should_not_be = ['часы', 'Портативная', 'Телевизор', 'Монитор', 'универсальная', 'Интерактивный',
                                        'Универсальное', 'сетевое', 'Беспроводное', 'Универсальное', 'автокрепление',
                                        'Автодержатель',
                                        'Держатель', 'Чехол', 'памяти', 'Защитное', 'стекло', 'Аудиосистема',
                                        'Беспроводные',
                                        'наушнники', 'Наушнники']
            for names in names_that_should_not_be:
                if names in item_title:
                    print(item_title, end='\n')
