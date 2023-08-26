import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Выберите язык из доступных: en, fr, ru')


@pytest.fixture(scope="function")
def driver(request):

    # Передача параметра окружения
    user_language = request.config.getoption("language")

    # Опции драйвера
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-cache")
    options.add_argument("--window-size=1200,700")

    """ Еесли хотите запустить драйвер в headless-режиме / раскомментируйте """
    # options.add_argument("--headless")

    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()
