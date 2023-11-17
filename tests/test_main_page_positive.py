import pytest
from pages.main_page import MainPage
from settings import *
from colorama import Fore, Style
import time


class TestMainPagePositive:
    @pytest.mark.one
    def test_search_products_positive(self, driver):
        """Позитивный тест проверки создания карточки питомца без фото. Валидация теста выполнена успешно в случае, если
        после ввода всех необходимых данных в форму карточки, пользователь остается на страницы path = "/my_pets", а
        карточка отображается в стеке питомцев пользователя со всеми переданными данными (без фото соответственно)."""
        page = MainPage(driver)
        time.sleep(2)
        page.enter_products_name("Iphone 14 pro")
        time.sleep(2)
        page.submit_search_btn_click()
        time.sleep(5)


