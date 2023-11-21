import pytest
from selenium.webdriver.chrome.options import *
from selenium import webdriver
from datetime import *
import os


@pytest.fixture(scope='function', autouse=True)
def duration_of_test(request):
    start_time = datetime.now()
    print(f'\n1/3) Начало выполнения тестовой функции: {start_time} сек.')
    yield
    end_time = datetime.now()
    print(f'\n2/3) Окончание выполнения тестовой функции: {end_time} сек.')
    print(f"\n3/3) ВСЕГО продолжительность теста {request.function.__name__}: {end_time - start_time} сек.\n")


@pytest.fixture()
def driver():
    """Pytest-фикстура(декоратор) для setup-запуска UI-тестов, спроектированных с помощью паттерна PageObjectModel и
    фреймворка Selenium. Определяет setup-настройки перед началом выполнения тестовой функции. Инициализирует
    запуск драйвера браузера Chrome, выполняет предварительную авторизацию пользователя на сайте (страница с path =
     = /login) c помощью ранее сформированного cookie-файла. Настоящая фикстура удобно реализует преимущества паттерна
    Page ObjectModel, позволяет осуществлять в UI-тестах вызов любых страниц сайта без необходимости каждый раз
    прописывать в тестовой функции скрипт авторизации, универсальна и применима в качестве аргумента к любой тестовой
    функции в рамках тестирования платформы petfriends.skillfactory.ru. Это ощутимо снижает время выполнения тестов,
    повышает восприятие и "читаемость" кода."""

    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    url = os.getenv("MAIN_URL") or "https://yandex.ru/maps/"
    driver.get(url)
    yield driver
    driver.quit()
