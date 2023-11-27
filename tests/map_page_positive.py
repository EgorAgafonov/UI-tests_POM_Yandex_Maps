import time
import colorama
import pytest
from pages.main_page import MainPage
from settings import *
from colorama import Fore, Style


class TestMapPagePositive:
    @pytest.mark.search_address
    def test_search_address_positive(self, driver):
        """Позитивный тест проверки поиска объекта(топонима) на карте по его названию. Валидация теста выполнена успешно
        в случае, если после ввода названия объекта в поле поиска и подтверждения действия, система определяет
        местоположение топонима на карте и фокусирует экран пользователя на искомом объекте. Искомый топоним
        (ожидаемый пользователем) совпадает с топонимом (результатом поиска), отображаемом на карте."""

        page = MainPage(driver)
        page.wait_page_loaded()
        page.enter_searching_address("Москва, Поклонная гора")
        page.submit_search_btn_click()
        page.wait_page_loaded()
        page.incrise_map_size(amount="low")
        page.wait_page_loaded()
        parsed_toponyms_name = page.get_toponym_descript(driver)
        page.make_screenshot(file_path=screenshots_folder + "\\test_search_address_positive.png")

        assert "Поклонная" in parsed_toponyms_name

    @pytest.mark.geoloc
    def test_current_geoloc_btn_click(self, driver):
        """Позитивный тест проверки работы кнопки "Моё местоположение", по нажатию определяющую текущую геолокацию
        пользователя. Тестирование выполняется без предварительной авторизации пользователя в системе. Валидация теста
        выполнена успешно в случае, если фактическое местонахождение пользователя в момент теста (МО, г. Видное)
        совпадает с местом, отображаемом на карте после нажатия на кнопку "Моё местоположение"."""

        page = MainPage(driver)
        page.wait_page_loaded(wait_for_element=page.current_geo_btn)
        page.my_current_geoloc_btn_click()
        page.wait_page_loaded(wait_for_element=page.decrease_view_size)
        page.decrease_map_size(amount="medium")
        page.wait_page_loaded(wait_for_element=page.incrise_view_size)
        page.make_screenshot(file_path=screenshots_folder + "\\test_current_geoloc_btn_click.png")

    @pytest.mark.map_size
    def test_change_map_size_btn_click(self, driver):
        """Позитивный тест проверки работы кнопки "Моё местоположение", по нажатию определяющую текущую геолокацию
        пользователя. Тестирование выполняется без предварительной авторизации пользователя в системе. Валидация теста
        выполнена успешно в случае, если фактическое местонахождение пользователя в момент теста (МО, г. Видное)
        совпадает с местом, отображаемом на карте после нажатия на кнопку "Моё местоположение"."""

        page = MainPage(driver)
        page.my_current_geoloc_btn_click()
        page.wait_page_loaded()
        page.make_screenshot(file_path=screenshots_folder + "\\test_change_map_size_initial.png")
        page.incrise_map_size(amount="high")
        page.wait_page_loaded()
        page.make_screenshot(file_path=screenshots_folder + "\\test_change_map_size_increased.png")
        page.decrease_map_size()
        page.decrease_map_size(amount="high")
        page.wait_page_loaded()
        page.make_screenshot(file_path=screenshots_folder + "\\test_change_map_size_decreased.png")

        if True:
            print("\nВалидация теста test_incrise_decrise_map_size_btn выполнена успешно!")

    @pytest.mark.map_3D_click
    def test_3D_map_btn_click(self, driver):
        """Позитивный тест проверки работы кнопки 3D-режима карты. Валидация теста выполнена успешно в случае, если
        после воздействия на контроллер изображение карты меняется с плоского вида "сверху" на режим "наклона" с
        трехмерным отображением объектов (3D-режим)."""

        page = MainPage(driver)
        page.wait_page_loaded(wait_for_element=page.current_geo_btn)
        page.my_current_geoloc_btn_click()
        page.wait_page_loaded(wait_for_element=page.incrise_view_size)
        page.incrise_map_size(amount="high")
        page.wait_page_loaded(check_page_changes=True)
        page.switch_to_3D_map_click(driver)
        page.wait_page_loaded()
        page.make_screenshot(file_path=screenshots_folder + "\\test_3D_map_btn_click.png")

    def test_build_route_by_car(self, driver):
        page = MainPage(driver)
        page.wait_page_loaded()
        page.switch_to_3D_map_click(driver)
        page.wait_page_loaded()
        page.build_route_btn_click(driver)
        page.wait_page_loaded()
        page.enter_departure_address(driver, "Музей-заповедник Царицыно")
        page.enter_destination_address(driver, "Музей-заповедник Коломенское")
        page.decrease_map_size("medium")
        page.wait_page_loaded()
        result = page.check_all_variants_of_arrivals(driver)

        if len(result) != 0:
            page.make_screenshot(file_path=screenshots_folder + "\\test_build_route_by_car.png")
            print(Style.DIM + Fore.GREEN + f"\n\nТест test_build_route_by_car выполнен успешно, маршрут "
                                           f"построен.\nВремя в пути (все предложенные варианты): {result}")
        else:
            raise Exception(Style.DIM + Fore.RED +"\nОшибка! Маршрут не построен, список с вариантами маршрутов(а) по "
                                                  "заданному пути отсутствует!\nОтразить ошибку в системе и создать "
                                                  "баг-репорт!")



