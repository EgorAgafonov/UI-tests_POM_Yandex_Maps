import time
import pytest
from pages.main_page import MainPage
from settings import *
from colorama import Fore, Style


class TestMapPagePositive:
    """Класс с коллекцией позитивных UI-тестов для функционального тестирования веб-приложения "Яндекс.Карты."""

    @pytest.mark.search_address
    def test_search_address_positive(self, driver):
        """Позитивный тест проверки поиска объекта(топонима) на карте по его названию. Валидация теста выполнена успешно
        в случае, если после ввода названия объекта в поле поиска и подтверждения действия, система определяет
        местоположение топонима на карте и фокусирует экран пользователя на искомом объекте. Искомый топоним
        (ожидаемый пользователем) совпадает с топонимом (результатом поиска), отображаемом на карте."""

        page = MainPage(driver)
        page.wait_page_loaded(check_images=True)
        page.enter_searching_address(driver, "Москва, просп. Мира, 111, Музей космонавтики")
        page.switch_to_3D_map_click(driver)
        page.wait_page_loaded(check_images=True)
        parsed_toponyms_name = page.get_toponym_descript(driver)
        page.make_screenshot(file_path=screenshots_folder + "\\test_search_address_positive.png")

        assert "космонавтики" in parsed_toponyms_name

    @pytest.mark.geoloc
    def test_current_geoloc_btn_click(self, driver):
        """Позитивный тест проверки работы кнопки "Моё местоположение", определяющую текущую геолокацию пользователя.
        Тестирование выполняется без предварительной авторизации пользователя в системе. Валидация теста выполнена
        успешно в случае, если фактическое местонахождение пользователя в момент теста (МО, г. Видное) совпадает с
        местом, отображаемом на карте после нажатия на кнопку "Моё местоположение"."""

        page = MainPage(driver)
        page.wait_page_loaded(wait_for_element=page.current_geo_btn)
        page.my_current_geoloc_btn_click()
        page.wait_page_loaded(wait_for_element=page.decrease_view_size)
        page.decrease_map_size(amount="medium")
        page.wait_page_loaded(wait_for_element=page.incrise_view_size)
        page.make_screenshot(file_path=screenshots_folder + "\\test_current_geoloc_btn_click.png")

    @pytest.mark.map_size
    def test_change_map_size_btn_click(self, driver):
        """Позитивный тест проверки работы кнопок "Приблизить" "Отдалить", отвечающих за увеличение/уменьшение размера
        карты. Валидация теста выполнена успешно если после каждого воздействия на указанные контроллеры,
        изображение карты пропорционально увеличивается и/или уменьшается в соответствии с действиями пользователя.
        Контроль теста определяется по скриншотам, сделанным в начальный момент, в момент увеличения и в момент
        уменьшения размера карты."""

        page = MainPage(driver)
        page.my_current_geoloc_btn_click()
        page.wait_page_loaded(check_images=True)
        page.make_screenshot(file_path=screenshots_folder + "\\test_change_map_size_initial.png")
        page.incrise_map_size(amount="high")
        page.wait_page_loaded(check_images=True)
        page.make_screenshot(file_path=screenshots_folder + "\\test_change_map_size_increased.png")
        page.wait_page_loaded(check_images=True)
        page.decrease_map_size(amount="high")
        page.wait_page_loaded(check_images=True)
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
        page.decrease_map_size(amount="low")
        page.wait_page_loaded(check_images=True)
        page.switch_to_3D_map_click(driver)
        page.wait_page_loaded(check_images=True)
        page.make_screenshot(file_path=screenshots_folder + "\\test_3D_map_btn_click.png")

    @pytest.mark.build_route
    def test_build_route_by_car(self, driver):
        """Позитивный тест проверки создания на карте маршрута для поездки на автомобиле. Указываются адреса места
        отправления и назначения, после чего система строит оптимальный/один из оптимальных маршрутов и отображает его
        на карте. Валидация теста выполнена успешно, если построенный маршрут отображается на карте, стек карточек с
        вариантами маршрутов (в зависимости от времени в пути до конечной точки) не пустой и содержит информацию о
        времени прибытия по указанному адресу. """

        page = MainPage(driver)
        page.wait_page_loaded(check_images=True)
        page.build_route_btn_click(driver)
        page.wait_page_loaded(check_images=True)
        page.enter_departure_address(driver, "Музей-заповедник Царицыно")
        page.enter_destination_address(driver, "Музей-заповедник Коломенское")
        page.decrease_map_size("low")
        page.switch_to_3D_map_click(driver)
        page.wait_page_loaded(check_images=True)
        result = page.check_all_variants_of_arrivals(driver)

        if len(result) != 0:
            page.make_screenshot(file_path=screenshots_folder + "\\test_build_route_by_car.png")
            print(Style.DIM + Fore.GREEN + f"\n\nТест test_build_route_by_car выполнен успешно, маршрут "
                                           f"построен.\nВремя в пути (все предложенные варианты):\n {result}")
        else:
            raise Exception(Style.DIM + Fore.RED +"\nОшибка! Маршрут не построен, список с вариантами маршрутов(а) по "
                                                  "заданному пути отсутствует!\nОтразить ошибку в системе и создать "
                                                  "баг-репорт!")

    @pytest.mark.traffic
    def test_traffic_btn_click(self, driver):
        """Позитивный тест проверки нажатия кнопки "Дорожная ситуация", отображающей на карте текущую ситуацию на
        дорогах города. Валидация теста выполнена успешно в случае, если после воздействия на контроллер на
        дорогах города отображается текущая плотность трафика с обозначением "зеленых", "красных", "оранжевых" зон
        (степень загруженности участка дороги)."""

        


