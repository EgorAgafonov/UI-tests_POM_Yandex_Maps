import pytest
from pages.main_page import MainPage
from settings import *
from datetime import *
from colorama import Fore, Style


class TestMapPagePositive:
    @pytest.mark.search_address
    def test_search_address_positive(self, driver):
        """Позитивный тест проверки поиска объекта(топонима) на карте по его названию. Валидация теста выполнена успешно
        в случае, если после ввода названия объекта в поле поиска и подтверждения действия, система определяет
        местоположение топонима на карте и фокусирует экран пользователя на искомом объекте. Искомый топоним
        (ожидаемый пользователем) совпадает с топонимом (результатом поиска), отображаемом на карте."""

        page = MainPage(driver)
        page.wait_page_loaded(check_images=True, check_page_changes=True)
        page.clear_search_field()
        page.enter_searching_address("Поклонная гора, Москва")
        page.submit_search_btn_click()
        parsed_toponyms_name = page.get_toponym_descript(driver)
        page.wait_page_loaded(check_images=True, check_page_changes=True)
        page.make_screenshot(file_path=screenshots_folder + "\\test_search_address_positive.png")

        assert "Поклонная гора" in parsed_toponyms_name

    @pytest.mark.geoloc
    def test_current_geoloc_no_auth(self, driver):
        """Позитивный тест проверки работы кнопки "Моё местоположение", по нажатию определяющую текущую геолокацию
        пользователя. Тестирование выполняется без предварительной авторизации пользователя в системе. Валидация теста
        выполнена успешно в случае, если фактическое местонахождение пользователя в момент теста (МО, г. Видное)
        совпадает с местом, отображаемом на карте после нажатия на кнопку "Моё местоположение"."""

        page = MainPage(driver)
        page.wait_page_loaded(check_images=True)
        page.my_current_geoloc_btn_click()
        page.wait_page_loaded(check_images=True)
        page.decrise_map_size(amount="medium")
        page.wait_page_loaded(check_images=True)
        page.make_screenshot(file_path=screenshots_folder + "\\test_current_geoloc_no_auth.png")

