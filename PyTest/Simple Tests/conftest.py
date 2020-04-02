import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser for test: Chrome or Firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None

    if browser_name == "chrome":
        print("\nStart Chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nStart Firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nQuit browser..")
    browser.quit()
