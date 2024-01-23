import pytest
from pages.main_page import MainPage
from settings import *
from colorama import Fore, Style
import allure
from allure_commons.types import LabelType


class TestMapPagePositive:
    """Класс с коллекцией UI-тестов для функционального тестирования веб-приложения "Яндекс.Карты."""

    @pytest.mark.search_address
    def test_search_address_positive(self, driver, toponyms_name="Москва, просп. Мира, 111, Музей космонавтики"):
        """Позитивный тест проверки поиска объекта(топонима) на карте по его названию. Валидация теста выполнена успешно
        в случае, если после ввода названия объекта в поле поиска и подтверждения действия, система определяет
        местоположение топонима на карте и фокусирует экран пользователя на искомом объекте. Искомый топоним
        (ожидаемый пользователем) совпадает с топонимом (результатом поиска), отображаемом на карте."""

        with allure.step("Шаг 1: Перейти на сайт https://yandex.ru/maps/.. и дождаться полной загрузки всех "
                         "элементов."):
            page = MainPage(driver)
            page.wait_page_loaded()
        with allure.step(f"Шаг 2: Ввести в поле поиска, выбрать из выпадающего списка название искомого топонима:\n"
                         f"{toponyms_name}."):
            page.enter_searching_address(driver, toponyms_name)
            page.wait_page_loaded()
            page.switch_to_3D_map_click(driver)
            page.incrise_map_size()
            page.wait_page_loaded()
        with allure.step("Шаг 3: Выполнить сравнение ожидаемого и фактического результатов теста."):
            parsed_toponyms_name = MainPage.get_toponym_descript(driver)
            if "космонавтики" not in parsed_toponyms_name:
                allure.attach(page.get_page_screenshot_PNG(),
                              name="search_address_FAILED",
                              attachment_type=allure.attachment_type.PNG)
                raise Exception("Названия(части названия) искомого топонима нет в результатах поиска системы!")
            else:
                assert "космонавтики" in parsed_toponyms_name
                page.make_screenshot(file_path=screenshots_folder + "\\test_search_address_positive.png")
                allure.attach(page.get_page_screenshot_PNG(),
                              name="search_address_PASSED",
                              attachment_type=allure.attachment_type.PNG)
                page.clear_searching_field(driver)

    @pytest.mark.geoloc
    def test_current_geoloc_btn_click(self, driver, current_geoloc='Видное'):
        """Позитивный тест проверки работы кнопки "Моё местоположение", определяющую текущую геолокацию пользователя.
        Тестирование выполняется без предварительной авторизации пользователя в системе. Аргумент current_geoloc должен
        содержать строчное наименование города(населенного пункта) с заглавной буквы, в котором пользователь находится
        в момент теста. Валидация теста выполнена успешно в случае, если место фактического местонахождения пользователя
        совпадает с местом, отображаемом на карте."""

        with allure.step("Шаг 1: Перейти на сайт https://yandex.ru/maps/.. и дождаться полной загрузки всех "
                         "элементов."):
            page = MainPage(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 2: Нажать на элемент 'Моё местоположение'(стрелка геолокации)."):
            page.my_current_geoloc_btn_click()
            page.wait_page_loaded()
            page.decrease_map_size(amount="high")
            page.wait_page_loaded()
            parsed_geoloc = page.get_current_geoloc_name(driver)
        with allure.step("Шаг 3: Выполнить сравнение ожидаемого и фактического результатов теста."):
            if parsed_geoloc not in current_geoloc:
                allure.attach(page.get_page_screenshot_PNG(),
                              name="current_geoloc_btn_click_FAILED",
                              attachment_type=allure.attachment_type.PNG)
                raise Exception(f"ОШИБКА! Определенное системой место геолокации пользователя: '{parsed_geoloc}', не "
                                f"совпадает с фактическим: '{current_geoloc}'.")
            else:
                assert parsed_geoloc in current_geoloc
                page.make_screenshot(file_path=screenshots_folder + "\\test_current_geoloc_btn_click.png")
                allure.attach(page.get_page_screenshot_PNG(),
                              name="current_geoloc_btn_click_PASSED",
                              attachment_type=allure.attachment_type.PNG)

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
        времени прибытия по указанному адресу."""

        page = MainPage(driver)
        page.wait_page_loaded(wait_for_element=page.current_geo_btn, check_images=True)
        page.build_route_btn_click(driver)
        page.wait_page_loaded(check_page_changes=True)
        page.enter_departure_address(driver, "Музей-заповедник Царицыно")
        page.wait_page_loaded(check_page_changes=True)
        page.enter_destination_address(driver, "Музей-заповедник Коломенское")
        page.wait_page_loaded(check_page_changes=True)
        page.switch_to_3D_map_click(driver)
        page.wait_page_loaded(check_page_changes=True)
        result = page.check_all_variants_of_arrivals(driver)

        if len(result) != 0:
            page.make_screenshot(file_path=screenshots_folder + "\\test_build_route_by_car.png")
            print(Style.DIM + Fore.GREEN + f"\n\nТест test_build_route_by_car выполнен успешно, маршрут "
                                           f"построен.\nВремя в пути (все предложенные варианты):\n {result}")
        else:
            raise Exception(Style.DIM + Fore.RED + "\nОшибка! Маршрут не построен, список с вариантами маршрутов(а) по "
                                                   "заданному пути отсутствует!\nОтразить ошибку в системе и создать "
                                                   "баг-репорт!")

    @pytest.mark.traffic
    def test_traffic_btn_click(self, driver):
        """Позитивный тест проверки нажатия кнопки "Дорожная ситуация", отображающей на карте текущую ситуацию на
        дорогах города. Валидация теста выполнена успешно в случае, если после воздействия на контроллер на
        дорогах города отображается текущая плотность трафика с обозначением "зеленых", "красных", "оранжевых" зон
        (степень загруженности участка дороги), контроллер кнопки отображает индекс загруженности по шкале 1/10."""

        page = MainPage(driver)
        page.wait_page_loaded(check_images=True)
        page.enter_searching_address(driver, "Москва, Садовое кольцо")
        page.wait_page_loaded(check_images=True)
        page.switch_to_3D_map_click(driver)
        page.wait_page_loaded(check_images=True)
        result = page.traffic_btn_click(driver)
        page.wait_page_loaded(check_images=True)

        if result:
            page.make_screenshot(file_path=screenshots_folder + "\\test_traffic_btn_click.png")
            print(Style.DIM + Fore.GREEN + f"\n Тест test_traffic_btn_click выполнен успешно!")
        else:
            raise Exception(Style.DIM + Fore.RED + f"\nОшибка! Трафик на карте не отображается, контроллер кнопки "
                                                   f"'Дорожная ситуация' не активен/не работает.\nОтразить ошибку в "
                                                   f"системе и создать баг-репорт!")

    @pytest.mark.city_trans
    def test_city_trans_btn_click(self, driver):
        """Позитивный тест проверки нажатия кнопки "Движущийся транспорт", отображающей на карте местоположение
        городского общественного транспорта с номером маршрута. Валидация теста выполнена успешно в случае, если
        после воздействия на контроллер кнопки, на карте отображаются иконки движущегося в реальном времени
        общественного транспорта с указанием маршрута."""

        page = MainPage(driver)
        page.wait_page_loaded(check_images=True, check_page_changes=True)
        page.enter_searching_address(driver, "Москва, ст. метро Домодедовская")
        page.wait_page_loaded(check_images=True)
        page.switch_to_3D_map_click(driver)
        result = page.city_transprt_btn_click(driver)
        page.wait_page_loaded(check_images=True)

        if result:
            page.make_screenshot(file_path=screenshots_folder + "\\test_city_trans_btn_click.png")
            print(Style.DIM + Fore.GREEN + f"\n Тест test_city_transprt_btn_click выполнен успешно!")
        else:
            raise Exception(Style.DIM + Fore.RED + f"\nОшибка! Иконки общественного транспорта на карте не отображаются,"
                                                   f" контроллер кнопки 'Движущийся транспорт' не активен/не работает."
                                                   f"\nОтразить ошибку в системе и создать баг-репорт!")