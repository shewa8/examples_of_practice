from pages.main_page import MainPage


def test_guest_can_change_language(browser):
    link = 'https://www.citrus.ua/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_change_language()
    page.should_be_language_link()
    page.should_be_uk_url()
