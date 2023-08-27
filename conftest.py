import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Выберите язык из доступных: en, fr, ru')
    parser.addoption('--browser', action='store', default='chrome', help='Выберите браузер: Chrome, Firefox')


@pytest.fixture(scope="function")
def driver(request):

    # Передача параметров окружения
    user_language = request.config.getoption("language")
    selected_browser = request.config.getoption("browser")

    if selected_browser == 'chrome':
        options = ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-cache")
        options.add_argument("--window-size=1200,700")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        
    elif selected_browser == 'firefox':
        options = FirefoxOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-cache")
        options.add_argument("--window-size=1200,700")
        profile = webdriver.FirefoxProfile()
        profile.set_preference("intl.accept_languages", user_language)
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options, firefox_profile=profile)
    else:
        raise ValueError("Неподдерживаемый браузер: {}".format(selected_browser))

    yield driver
    driver.quit()
