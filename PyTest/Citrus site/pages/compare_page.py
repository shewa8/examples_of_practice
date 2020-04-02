from pages.base_page import BasePage
from pages.base_page import Env
from pages.base_page import LogFile
from pages.locators import ComparePageLocators
import time


class ComparePage(BasePage):
    def add_to_compare(self):
        LogFile.logger.info('Guest going to add product for compare')
        add_to_compare = self.element_to_be_clickable(*ComparePageLocators.ADD_TO_COMPARE)
        assert add_to_compare, LogFile.logger.error(f'Element {ComparePageLocators.ADD_TO_COMPARE} not found')
        add_to_compare.click()
        LogFile.logger.info('Guest successfully added product for compare')
        time.sleep(Env.vars['wait_time'])

    def go_to_compare_page(self):
        LogFile.logger.info('Guest going to compare page')
        go_to_compare = self.element_to_be_clickable(*ComparePageLocators.GO_TO_COMPARE)
        assert go_to_compare, LogFile.logger.error(f'Element {ComparePageLocators.GO_TO_COMPARE} not found')
        go_to_compare.click()
        LogFile.logger.info('Guest successfully pass to compare page')
        time.sleep(Env.vars['wait_time'])

    def delete_from_compare(self):
        LogFile.logger.info('Guest going to delete product from compare')
        time.sleep(Env.vars['wait_time'])
        delete_first_item = self.element_to_be_clickable(*ComparePageLocators.DELETE_ITEM)
        assert delete_first_item, LogFile.logger.error(f'Element {ComparePageLocators.DELETE_ITEM} not found')
        delete_first_item.click()
        LogFile.logger.info('Guest successfully deleted product from compare page')

    def verify_compare_counter(self):
        LogFile.logger.info('Go to main page and verify compare counter after removing products from compare page')
        compare_counter = self.element_to_be_present(*ComparePageLocators.COMPARE_COUNTER)
        assert compare_counter, LogFile.logger.error(f'Element {ComparePageLocators.COMPARE_COUNTER} not found')
        get_value = compare_counter.text
        assert get_value == '0', \
            LogFile.logger.error(f'Compare counter should be "0", but still shows "{get_value}"')
        time.sleep(Env.vars['wait_time'])
        LogFile.logger.info('Compare counter is disappeared')
