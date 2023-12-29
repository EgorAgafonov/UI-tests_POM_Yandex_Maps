import pytest
from selenium.webdriver.chrome.options import *
from selenium import webdriver
from datetime import *
from colorama import Fore, Style, Back
import os


@pytest.fixture(scope='function', autouse=True)
def duration_of_test(request):
    start_time = datetime.now()
    print(f'\n1/3) Начало выполнения тестовой функции: {start_time} сек.')
    yield
    end_time = datetime.now()
    print(f'\n2/3) Окончание выполнения тестовой функции: {end_time} сек.')
    print(Fore.BLACK + Style.BRIGHT + Back.YELLOW + f"3/3) ВСЕГО продолжительность теста {request.function.__name__}: "
                                                    f"{end_time - start_time} сек.")


@pytest.fixture(scope='function')
def driver():
    """Pytest-фикстура(декоратор) для выполнения UI-тестов, спроектированных с помощью паттерна PageObjectModel и
    фреймворка Selenium в рамках тестирования платформы "Yandex Карты". Определяет setup-настройки перед началом
    выполнения тестовой функции, инициализирует запуск драйвера браузера Chrome и передает его в любую тестовую функцию
    коллекции как объект класса webdriver фреймворка Selenium."""

    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    url = os.getenv("MAIN_URL") or "https://yandex.ru/maps/"
    driver.get(url)
    yield driver
    # driver.quit()
