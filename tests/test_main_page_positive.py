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
        page.clear_search_field()
        page.enter_searching_address("Музей ВВС, Монино")
        page.submit_search_btn_click()
        parsed_toponym = str(page.get_toponym_descript(driver))
        assert "воздушных" in parsed_toponym
        page.make_screenshot()

