import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                 help="Choose language code")
    parser.addoption('--timeout', action='store', default=10,
                 help="Choose timeout time (seconds)")
                 
@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    timeout = request.config.getoption("timeout")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(executable_path='C:/Users/ХХХ/Desktop/Учеба/Сафаров/Python/chromedriver.exe')
    browser.implicitly_wait(timeout)
    
    yield browser
    
    print("\nquit browser..")
    browser.quit()

# @pytest.fixture(scope="function")
# def timeout(request):
    # return request.config.getoption("timeout")
    