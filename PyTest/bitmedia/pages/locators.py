from selenium.webdriver.common.by import By


class ProductPageLocatots:
    ITEM_PAGE = (By.CSS_SELECTOR, '#homefeatured > li:nth-child(4) a.product_img_link')
    NAME_OF_PRODUCT = (By.TAG_NAME, 'h1')
    SELECT_SIZE = (By.TAG_NAME, 'select')
    ADD_CART = (By.CSS_SELECTOR, '#add_to_cart')
    CHECKOUT_BTN = (By.CSS_SELECTOR, '.button-medium')
    IN_STOCK = (By.CSS_SELECTOR, '.label-success')
    CHECKOUT_BTN_2 = (By.XPATH, '//*[@id="center_column"]/p[2]/a[1]/span')
    ORDER_COMPLETE = (By.CSS_SELECTOR, '.cheque-indent .dark')


class RegNewCustomer:
    CREATE_ACC = (By.CSS_SELECTOR, '#email_create')
    CREATE_SUBMIT_BTN = (By.CSS_SELECTOR, '#SubmitCreate')
    FIRST_NAME = (By.CSS_SELECTOR, '#customer_firstname')
    LAST_NAME = (By.CSS_SELECTOR, '#customer_lastname')
    PASSWD = (By.CSS_SELECTOR, '#passwd')
    ADRESS = (By.CSS_SELECTOR, '#address1')
    CITY = (By.CSS_SELECTOR, '#city')
    STATE = (By.CSS_SELECTOR, '#id_state')
    POSTCODE = (By.CSS_SELECTOR, '#postcode')
    PHONE_NUMBER = (By.CSS_SELECTOR, '#phone_mobile')
    SUMBIT_BTN = (By.CSS_SELECTOR, '#submitAccount')
    CHECKOUT_BTN = (By.XPATH, '//*[@id="center_column"]/form/p/button/span')


class ShippingAgree:
    CHECK_BOX_AGREE = (By.CSS_SELECTOR, '#cgv')
    CHECKOUT_BTN = (By.XPATH, '//*[@id="form"]/p/button/span')
    PAYMENT = (By.CSS_SELECTOR, '.bankwire')
    CONFIRM_ORDER = (By.XPATH, '//*[@id="cart_navigation"]/button/span')
