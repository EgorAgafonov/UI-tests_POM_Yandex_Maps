import pytest
from pages.main_page import MainPage
from settings import *
from colorama import Fore, Style
import time


class TestMainPagePositive:
    @pytest.mark.one
    def test_search_info_positive(self, driver):
        """Позитивный тест проверки создания карточки питомца без фото. Валидация теста выполнена успешно в случае, если
        после ввода всех необходимых данных в форму карточки, пользователь остается на страницы path = "/my_pets", а
        карточка отображается в стеке питомцев пользователя со всеми переданными данными (без фото соответственно)."""

        page = MainPage(driver)
        time.sleep(2)
        page.my_current_geoloc_btn_click()
        time.sleep(2)
        page.incrise_map_size()
        time.sleep(2)
        page.clear_search_field()
        page.enter_searching_address("Москва, Красная площадь")
        page.submit_search_btn_click()
        time.sleep(2)
        page.dicrise_map_size()
        page.make_screenshot()

