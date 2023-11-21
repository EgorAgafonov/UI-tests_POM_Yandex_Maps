import pytest
from pages.main_page import MainPage
from settings import *
from colorama import Fore, Style
import time


class TestMainPagePositive:
    @pytest.mark.one
    def test_search_address_positive(self, driver):
        """Позитивный тест проверки поиска объекта(топонима) на карте по его названию. Валидация теста выполнена успешно
        в случае, если после ввода названия объекта в поле поиска и подтверждения действия, система определяет
        местоположение топонима на карте и фокусирует экран пользователя на искомом объекте. Искомый топоним
        (ожидаемый пользователем) совпадает с топонимом (результатом поиска), отображаемом на карте."""

        page = MainPage(driver)
        time.sleep(2)
        page.my_current_geoloc_btn_click()
        time.sleep(2)
        page.incrise_map_size(amount="low")
        time.sleep(2)
        page.clear_search_field()
        page.enter_searching_address("Москва, Красная площадь")
        page.submit_search_btn_click()
        time.sleep(2)
        page.dicrise_map_size(amount="medium")
        time.sleep(5)
        page.make_screenshot()

