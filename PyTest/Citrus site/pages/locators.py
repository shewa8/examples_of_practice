from selenium.webdriver.common.by import By


class BasePageLocators:
    LANGUAGE_LINK = (By.CSS_SELECTOR, '.language > a')
    GO_TO_MAIN_PAGE = (By.CSS_SELECTOR, '.logo')


class MainPageLocators:
    LANGUAGE_LINK = (By.CSS_SELECTOR, '.language > a')


class ProductPageLocators:
    PRODUCT_LINK = (By.CSS_SELECTOR, '.menu-aim__item:nth-child(3)')  # change number for change product's catalog
    PRODUCT_LINK_2 = (
        By.CSS_SELECTOR, '.ui-categories__body > :nth-child(1)')  # change number for change product's catalog
    PRODUCT_LINK_3 = (
        By.CSS_SELECTOR, '.ui-categories__body >  :nth-child(1)')  # change number for change product's catalog
    ITEM_PAGE_1 = (By.CSS_SELECTOR, 'div:nth-child(7) .product-card__name > a')  # change number for change product
    ITEM_PAGE_2 = (By.CSS_SELECTOR, 'div:nth-child(8) .product-card__name > a')  # change number for change product
    ADD_TO_BASKET = (By.CSS_SELECTOR, '#buy-block .normal button')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product__title')
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, '.ctrs-basket-product__name')
    LIST_OF_ITEMS = (By.CSS_SELECTOR, '.product-card__name > a')
    CATALOG_CARD = (By.CSS_SELECTOR, '.catalog-card-container')
    SKIP_BUTTON = (By.CSS_SELECTOR, '.pagination-container > ul:nth-child(1) a:nth-child(1)')


class ComparePageLocators:
    ADD_TO_COMPARE = (By.CSS_SELECTOR, '.showcase__actions button:nth-child(2)')
    GO_TO_COMPARE = (By.CSS_SELECTOR, '.user-actions__compare')
    DELETE_ITEM = (By.CSS_SELECTOR, '.base-column div:nth-child(2) > i:nth-child(1)')
    COMPARE_COUNTER = (By.CSS_SELECTOR, '.icon-comparison2 .counter')
