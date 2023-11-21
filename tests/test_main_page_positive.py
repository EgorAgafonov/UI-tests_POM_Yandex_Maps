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
        page.wait_page_loaded(check_images=True)
        page.clear_search_field()
        page.enter_searching_address("Поклонная гора, Москва")
        page.submit_search_btn_click()
        page.wait_page_loaded(check_images=True)
        parsed_toponym = str(page.get_toponym_descript(driver))
        page.make_screenshot()

        assert "гора" in parsed_toponym

