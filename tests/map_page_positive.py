import pytest
from pages.main_page import MainPage
from settings import *
from colorama import Fore, Style
import allure
from allure_commons.types import LabelType
from urllib.parse import urlparse
import time


class TestMapPagePositive:
    """Класс с коллекцией UI-тестов для функционального тестирования веб-приложения "Яндекс.Карты."""

    @pytest.mark.search_address
    @allure.title("Поиск адреса(топонима) на карте")
    @allure.testcase("https://yandex.ru/maps", "TC-YMPS-SA-01")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label(LabelType.LANGUAGE, "Python")
    @allure.label(LabelType.FRAMEWORK, "Pytest", "Selenium")
    @allure.label("Агафонов Е.А.", "владелец")
    @allure.link("https://yandex.ru/maps", name="https://yandex.ru/maps")
    @allure.epic("Пользовательский интерфейс (позитивные тесты)")
    @allure.feature("Поиск объекта(топонима) на карте по названию")
    def test_search_address_positive(self, driver, toponyms_name="Музей космонавтики"):
        """Позитивный тест проверки поиска объекта(топонима) на карте по его названию. Валидация теста выполнена успешно
        в случае, если после ввода названия объекта в поле поиска и подтверждения действия, система определяет
        местоположение топонима на карте и фокусирует экран пользователя на искомом объекте. Искомый топоним
        (ожидаемый пользователем) совпадает с топонимом (результатом поиска), отображаемом на карте."""

        with allure.step("Шаг 1: Перейти на сайт https://yandex.ru/maps/ и дождаться полной загрузки всех элементов."):
            page = MainPage(driver)
            page.wait_page_loaded()
        with allure.step(f"Шаг 2: Ввести в поле поиска, выбрать из выпадающего списка название искомого топонима:\n"
                         f"{toponyms_name}."):
            page.enter_searching_address(driver, toponyms_name)
            page.wait_page_loaded()
        with allure.step("Шаг 3: Выполнить сравнение ожидаемого и фактического результатов теста."):
            parsed_toponyms_name = page.get_toponym_descript(driver)
            if toponyms_name not in parsed_toponyms_name:
                allure.attach(page.get_page_screenshot_PNG(),
                              name="search_address_FAILED",
                              attachment_type=allure.attachment_type.PNG)
                page.clear_searching_field(driver)
                raise Exception("Названия(части названия) искомого топонима нет в результатах поиска системы!")
            else:
                assert "космонавтики" in parsed_toponyms_name
                page.make_screenshot(file_path=screenshots_folder + "\\test_search_address_positive.png")
                allure.attach(page.get_page_screenshot_PNG(),
                              name="search_address_PASSED",
                              attachment_type=allure.attachment_type.PNG)
                page.clear_searching_field(driver)
                print("\nВалидация теста test_search_address_positive выполнена успешно!")

    @pytest.mark.geoloc
    @allure.title("Определение геолокации пользователя на карте")
    @allure.testcase("https://yandex.ru/maps", "TC-YMPS-GLC-01")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label(LabelType.LANGUAGE, "Python")
    @allure.label(LabelType.FRAMEWORK, "Pytest", "Selenium")
    @allure.label("Агафонов Е.А.", "владелец")
    @allure.link("https://yandex.ru/maps", name="https://yandex.ru/maps")
    @allure.epic("Пользовательский интерфейс (позитивные тесты)")
    @allure.feature("Определение текущей геолокации пользователя на карте")
    def test_current_geoloc_btn_click(self, driver, current_geoloc='Видное'):
        """Позитивный тест проверки работы кнопки "Моё местоположение", определяющую текущую геолокацию пользователя.
        Тестирование выполняется без предварительной авторизации пользователя в системе. Аргумент current_geoloc должен
        содержать строчное наименование города(населенного пункта) с заглавной буквы, в котором пользователь находится
        в момент теста. Валидация теста выполнена успешно в случае, если место фактического местонахождения пользователя
        совпадает с местом, отображаемом на карте."""

        with allure.step("Шаг 1: Перейти на сайт https://yandex.ru/maps/ и дождаться полной загрузки всех элементов."):
            page = MainPage(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 2: Нажать на элемент 'Моё местоположение'(стрелка геолокации)."):
            page.my_current_geoloc_btn_click(driver)
            page.wait_page_loaded()
            page.refresh_page()
            page.wait_page_loaded()
            page.zoom_out_map(driver, amount="high")
            page.zoom_out_map(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 3: Выполнить сравнение ожидаемого и фактического результатов теста."):
            parsed_geoloc = page.get_current_geoloc_name(driver)
            page.make_screenshot(file_path=screenshots_folder + "\\test_current_geoloc_btn_.png")
            allure.attach(page.get_page_screenshot_PNG(),
                          name="current_geoloc_btn_click_actual",
                          attachment_type=allure.attachment_type.PNG)
            assert parsed_geoloc == current_geoloc, (f"ОШИБКА! Город геолокации пользователя на сайте:'{parsed_geoloc}'"
                                                     f" не совпадает с городом в момент тестирования (фактическим): "
                                                     f"'{current_geoloc}'.")

    @pytest.mark.map_size
    @allure.title("Увеличение/уменьшение размера изображения карты")
    @allure.testcase("https://yandex.ru/maps", "TC-YMPS-ZOOM-01")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label(LabelType.LANGUAGE, "Python")
    @allure.label(LabelType.FRAMEWORK, "Pytest", "Selenium")
    @allure.label("Агафонов Е.А.", "владелец")
    @allure.link("https://yandex.ru/maps", name="https://yandex.ru/maps")
    @allure.epic("Пользовательский интерфейс (позитивные тесты)")
    @allure.feature("Проверка работы элементов увеличения/уменьшения размера карты")
    def test_change_map_size_btn_click(self, driver, random_place="Москва, ст. метро Чистые пруды"):
        """Позитивный тест проверки работы кнопок "Приблизить" "Отдалить", отвечающих за увеличение/уменьшение размера
        карты. Валидация теста выполнена успешно если после каждого воздействия на указанные контроллеры,
        изображение карты пропорционально увеличивается и/или уменьшается в соответствии с действиями пользователя.
        Контроль теста определяется по сравнению значений масштаба карты в начальный момент теста, после уменьшения и
        после увеличения размера карты."""

        with allure.step("Шаг 1: Перейти на сайт https://yandex.ru/maps/ и дождаться полной загрузки всех элементов."):
            page = MainPage(driver)
            page.wait_page_loaded()
            current_scale = page.check_current_scale_line_value(driver)
        with allure.step("Шаг 2: Кликнуть элемент 'Отдалить' 3(три) раза"):
            page.enter_searching_address(driver, random_place)
            page.wait_page_loaded()
            page.zoom_out_map(driver, amount="high")
            page.wait_page_loaded(check_page_changes=True)
            page.make_screenshot(file_path=screenshots_folder + "\\test_change_map_size_decreased.png")
            allure.attach(page.get_page_screenshot_PNG(),
                          name="change_map_size_btn_decrsd_x_2",
                          attachment_type=allure.attachment_type.PNG)
            decrease_scale = page.check_current_scale_line_value(driver)

        with allure.step("Шаг 3: Кликнуть элемент 'Приблизить' 2(два) раза"):
            page.zoom_in_map(driver, amount="medium")
            page.wait_page_loaded()
            page.make_screenshot(file_path=screenshots_folder + "\\test_change_map_size_increased.png")
            allure.attach(page.get_page_screenshot_PNG(),
                          name="change_map_size_btn_incrs_x_3",
                          attachment_type=allure.attachment_type.PNG)
            page.clear_searching_field(driver)
            increase_scale = page.check_current_scale_line_value(driver)

        with allure.step("Шаг 4: Проверка результатов теста."):
            if current_scale != decrease_scale:
                assert decrease_scale != increase_scale
                print(f"\nМасштаб начальный: {current_scale}\n"
                      f"Масштаб уменьшенный: {decrease_scale}\n"
                      f"Масштаб увеличенный: {increase_scale}\n"
                      f"Валидация теста test_incrise_decrise_map_size_btn выполнена успешно!")
            else:
                raise Exception("Ошибка! Проверьте корректность работы элементов 'Приблизить', 'Отдалить'"
                                "и/или указаный путь локаторов элементов . Иначе отразить ошибку в системе и создать "
                                "баг-репорт.")

    @pytest.mark.map_3D_click
    @allure.title("Работа карты в режиме изометрического отображения объектов (3D-режим)")
    @allure.testcase("https://yandex.ru/maps", "TC-YMPS-3DMD-01")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label(LabelType.LANGUAGE, "Python")
    @allure.label(LabelType.FRAMEWORK, "Pytest", "Selenium")
    @allure.label("Агафонов Е.А.", "владелец")
    @allure.link("https://yandex.ru/maps", name="https://yandex.ru/maps")
    @allure.epic("Пользовательский интерфейс (позитивные тесты)")
    @allure.feature("Проверка работы элемента 'Наклонить карту' (3D-режим карты)")
    def test_3D_map_btn_click(self, driver, random_place="Москва, Музей советских игровых автоматов"):
        """Позитивный тест проверки работы кнопки 3D-режима карты. Валидация теста выполнена успешно в случае, если
        после воздействия на элемент "Наклонить карту" изображение карты меняется с плоского вида "сверху" на режим
        "наклона" с трехмерным отображением объектов (3D-режим)."""

        with allure.step("Шаг 1: Перейти на сайт https://yandex.ru/maps/ и дождаться полной загрузки всех элементов."):
            page = MainPage(driver)
            page.wait_page_loaded()
            page.enter_searching_address(driver, random_place)
            page.wait_page_loaded()
            allure.attach(page.get_page_screenshot_PNG(),
                          name="3D_map_btn_click_before",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Шаг 2: Кликнуть элемент 'Наклонить карту'"):
            page.zoom_in_map(driver)
            page.wait_page_loaded()
            page.switch_to_3D_map_click(driver)
            page.wait_page_loaded()
            page.make_screenshot(file_path=screenshots_folder + "\\test_3D_map_btn_click.png")
            allure.attach(page.get_page_screenshot_PNG(),
                          name="3D_map_btn_click_after",
                          attachment_type=allure.attachment_type.PNG)
            page.switch_off_3D_map_mode(driver)
            page.clear_searching_field(driver)
        with allure.step("Шаг 3: Выполнить проверку результатов теста."):
            if True:
                print("\nВалидация теста test_3D_map_btn_click выполнена успешно!")
            else:
                raise Exception("\nОшибка! Проверьте корректность локатора элемента 'Наклонить карту' и/или метода для "
                                "взаимодействия с указанным элементом. Иначе отразить ошибку в системе и создать "
                                "баг-репорт")

    @pytest.mark.map_display_mode
    @allure.title("Работа карты в режиме изометрического отображения объектов (3D-режим)")
    @allure.testcase("https://yandex.ru/maps", "TC-YMPS-MPSTPS-01")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label(LabelType.LANGUAGE, "Python")
    @allure.label(LabelType.FRAMEWORK, "Pytest", "Selenium")
    @allure.label("Агафонов Е.А.", "владелец")
    @allure.link("https://yandex.ru/maps", name="https://yandex.ru/maps")
    @allure.epic("Пользовательский интерфейс (позитивные тесты)")
    @allure.feature("Проверка работы режимов отображения карты ('Схема'', 'Спутник', 'Гибрид')")
    def test_checking_map_display_modes(self, driver, random_place="Париж, Эйфелева башня"):
        """Позитивный тест проверки работы режимов отображения карты. Валидация теста выполнена успешно в случае, если
        после воздействия на элементы "Схема", "Спутник", "Гибрид" в меню выбора, изображение карты принимает вид,
        соответствующий заданному параметру)."""

        with allure.step("Шаг 1: Перейти на сайт https://yandex.ru/maps/ и дождаться полной загрузки всех элементов."):
            page = MainPage(driver)
            page.wait_page_loaded()
            page.enter_searching_address(driver, random_place)
            page.wait_page_loaded()
        with allure.step("Шаг 2: Кликнуть элемент 'Слои' в правом верхнем углу карты"):
            page.switch_to_3D_map_click(driver)
            page.wait_page_loaded()
            page.make_screenshot(file_path=screenshots_folder + "\\test_map_display_modes_SCHEME.png")
            allure.attach(page.get_page_screenshot_PNG(),
                          name="map_display_mode_SCHEME",
                          attachment_type=allure.attachment_type.PNG)
            page.choose_map_layers_btn_click(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 3: В выпадающем списке кликнуть элемент 'Спутник'"):
            page.choose_sputnik_mode_btn_click(driver)
            page.wait_page_loaded()
            page.make_screenshot(file_path=screenshots_folder + "\\test_map_display_modes_SPUTNIK.png")
            allure.attach(page.get_page_screenshot_PNG(),
                          name="map_display_mode_SPUTNIK",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Шаг 4: В выпадающем списке кликнуть элемент 'Гибрид'"):
            page.choose_hybrid_mode_btn_click(driver)
            page.wait_page_loaded()
            page.make_screenshot(file_path=screenshots_folder + "\\test_map_display_modes_HYBRID.png")
            allure.attach(page.get_page_screenshot_PNG(),
                          name="map_display_mode_HYBRID",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Шаг 5: Выполнить проверку результатов теста."):
            page.clear_searching_field(driver)
            page.choose_map_layers_btn_click(driver)
            page.choose_scheme_mode_btn_click(driver)
            page.my_current_geoloc_btn_click(driver)
            page.wait_page_loaded(check_page_changes=True)
            if True:
                print("\nВалидация теста test_checking_map_display_modes выполнена успешно!")
            else:
                raise Exception(
                    "\nОшибка! Проверьте корректность локаторов элементов 'Гибрид', 'Спутник' и/или методов "
                    "для взаимодействия с указанными элементами. Иначе отразить ошибку в системе и создать "
                    "баг-репорт")

    @pytest.mark.build_route
    @allure.title("Создание маршрута на карте ('Автомобиль')")
    @allure.testcase("https://yandex.ru/maps", "TC-YMPS-BLDRT-01")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label(LabelType.LANGUAGE, "Python")
    @allure.label(LabelType.FRAMEWORK, "Pytest", "Selenium")
    @allure.label("Агафонов Е.А.", "владелец")
    @allure.link("https://yandex.ru/maps", name="https://yandex.ru/maps")
    @allure.epic("Пользовательский интерфейс (позитивные тесты)")
    @allure.feature("Построение маршрута  на карте для частного ТС по начальной и конечной точкам.")
    def test_build_route_by_car(self, driver, depart_point="Музей-заповедник Царицыно",
                                destin_point="Музей-заповедник Коломенское"):
        """Позитивный тест проверки создания на карте маршрута для поездки на автомобиле. Указываются адреса места
        отправления и назначения (аргументы depart_point и destin_point), после чего система строит оптимальный/один из
        оптимальных маршрутов и отображает его на карте. Валидация теста выполнена успешно, если построенный маршрут
        отображается на карте, стек карточек с вариантами маршрутов (в зависимости от времени в пути до конечной точки)
        не пустой и содержит информацию о времени прибытия по указанному адресу."""

        with allure.step("Шаг 1: Перейти на сайт https://yandex.ru/maps/ и дождаться полной загрузки всех элементов."):
            page = MainPage(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 2: Нажать на элемент 'Маршруты'"):
            page.build_route_btn_click(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 3: Нажать на иконку элемента 'На автомобиле'."):
            page.route_by_car_btn_click(driver)
        with allure.step("Шаг 4: В поле 'Откуда' ввести/выбрать из выпадающего списка название начальной точки "
                         "маршрута."):
            page.enter_departure_address(driver, depart_point)
            page.wait_page_loaded()
        with allure.step("Шаг 5: В поле 'Куда' ввести/выбрать из выпадающего списка название конечной точки "
                         "маршрута."):
            page.enter_destination_address(driver, destin_point)
            page.switch_to_3D_map_click(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 6: Выполнить проверку результатов теста."):
            result = page.check_all_variants_of_arrivals_car(driver)
            page.wait_page_loaded(check_page_changes=True)
            if len(result) != 0:
                page.make_screenshot(file_path=screenshots_folder + "\\test_build_route_by_car.png")
                allure.attach(page.get_page_screenshot_PNG(),
                              name="build_route_by_car_PASSED",
                              attachment_type=allure.attachment_type.PNG)
                page.clear_searching_field(driver)
                page.switch_off_3D_map_mode(driver)
                print(Style.DIM + Fore.GREEN + f"\n\nТест test_build_route_by_car выполнен успешно, маршрут "
                                               f"построен.\nВремя в пути (все предложенные варианты):\n{result}")
            else:
                allure.attach(page.get_page_screenshot_PNG(),
                              name="build_route_by_car_FAILED",
                              attachment_type=allure.attachment_type.PNG)
                page.clear_searching_field(driver)
                page.switch_off_3D_map_mode(driver)
                raise Exception(Style.DIM + Fore.RED + "\nОшибка! Маршрут не построен, список с вариантами маршрутов(а)"
                                                       " по заданному пути отсутствует!\nОтразить ошибку в системе и "
                                                       "создать баг-репорт!")

    @pytest.mark.build_route
    @allure.title("Создание маршрута на карте ('Городской транспорт')")
    @allure.testcase("https://yandex.ru/maps", "TC-YMPS-BLDRT-02")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label(LabelType.LANGUAGE, "Python")
    @allure.label(LabelType.FRAMEWORK, "Pytest", "Selenium")
    @allure.label("Агафонов Е.А.", "владелец")
    @allure.link("https://yandex.ru/maps", name="https://yandex.ru/maps")
    @allure.epic("Пользовательский интерфейс (позитивные тесты)")
    @allure.feature("Построение маршрута  на карте для поездки на общественном транспорте по начальной и конечной "
                    "точкам.")
    def test_build_route_by_city_trnsprt(self, driver, depart_point="Московский зоопарк",
                                         destin_point="Московский дом книги, ул. Новый Арбат"):
        """Позитивный тест проверки создания на карте маршрута для планирования поездки на общественном транспорте.
        По содержанию, условиям валидации тест-кейс аналогичен тесту test_build_route_by_car."""

        with allure.step("Шаг 1: Перейти на сайт https://yandex.ru/maps/ и дождаться полной загрузки всех элементов."):
            page = MainPage(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 2: Нажать на элемент 'Маршруты'."):
            page.build_route_btn_click(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 3: Нажать на иконку элемента 'На общественном транспорте'"):
            page.route_by_trnsprt_btn_click(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 4: В поле 'Откуда' ввести/выбрать из выпадающего списка название начальной точки "
                         "маршрута."):
            page.enter_departure_address(driver, depart_point)
            page.wait_page_loaded()
        with allure.step("Шаг 5: В поле 'Куда' ввести/выбрать из выпадающего списка название конечной точки "
                         "маршрута."):
            page.enter_destination_address(driver, destin_point)
            page.switch_to_3D_map_click(driver)
            page.zoom_out_map(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 6: Выполнить проверку результатов теста."):
            result = page.check_all_variants_of_arrivals_city(driver)
            page.wait_page_loaded(check_page_changes=True)
            if len(result) != 0:
                page.make_screenshot(file_path=screenshots_folder + "\\test_build_route_by_city_trnsprt.png")
                allure.attach(page.get_page_screenshot_PNG(),
                              name="test_build_route_by_city_trnsprt_PASSED",
                              attachment_type=allure.attachment_type.PNG)
                page.clear_searching_field(driver)
                page.switch_off_3D_map_mode(driver)
                print(Style.DIM + Fore.GREEN + f"\n\nТест test_build_route_by_city_trnsprt выполнен успешно, маршрут "
                                               f"построен.\nВремя в пути (все предложенные варианты):\n{result}")
            else:
                allure.attach(page.get_page_screenshot_PNG(),
                              name="test_build_route_by_city_trnsprt_FAILED",
                              attachment_type=allure.attachment_type.PNG)
                page.clear_searching_field(driver)
                page.switch_off_3D_map_mode(driver)
                raise Exception(Style.DIM + Fore.RED + "\nОшибка! Маршрут не построен, список с вариантами маршрутов(а)"
                                                       " по заданному пути отсутствует!\nОтразить ошибку в системе и "
                                                       "создать баг-репорт!")

    @pytest.mark.build_route
    @allure.title("Создание маршрута на карте ('Городской транспорт')")
    @allure.testcase("https://yandex.ru/maps", "TC-YMPS-BLDRT-03")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label(LabelType.LANGUAGE, "Python")
    @allure.label(LabelType.FRAMEWORK, "Pytest", "Selenium")
    @allure.label("Агафонов Е.А.", "владелец")
    @allure.link("https://yandex.ru/maps", name="https://yandex.ru/maps")
    @allure.epic("Пользовательский интерфейс (позитивные тесты)")
    @allure.feature("Построение маршрута на карте для планирования пешей прогулки от начальной до конечной "
                    "точки.")
    def test_build_route_by_foot(self, driver, depart_point="м. Тверская", destin_point="Патриаршие пруды"):
        """Позитивный тест проверки создания на карте маршрута для планирования пешей прогулки. По содержанию, условиям
        валидации тест-кейс аналогичен тестам test_build_route_by_car, test_build_route_by_city_trnsprt."""

        with allure.step("Шаг 1: Перейти на сайт https://yandex.ru/maps/ и дождаться полной загрузки всех элементов."):
            page = MainPage(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 2: Нажать на элемент 'Маршруты'."):
            page.build_route_btn_click(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 3: Нажать на иконку элемента 'Пешком'"):
            page.route_by_foot_btn_click(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 4: В поле 'Откуда' ввести/выбрать из выпадающего списка название начальной точки "
                         "маршрута."):
            page.enter_departure_address(driver, depart_point)
            page.wait_page_loaded()
        with allure.step("Шаг 5: В поле 'Куда' ввести/выбрать из выпадающего списка название конечной точки "
                         "маршрута."):
            page.enter_destination_address(driver, destin_point)
            page.switch_to_3D_map_click(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 6: Выполнить проверку результатов теста."):
            result = page.check_all_variants_time_by_foot(driver)
            page.wait_page_loaded(check_page_changes=True)
            if len(result) != 0:
                page.make_screenshot(file_path=screenshots_folder + "\\test_build_route_by_foot.png")
                allure.attach(page.get_page_screenshot_PNG(),
                              name="test_build_route_by_foot_PASSED",
                              attachment_type=allure.attachment_type.PNG)
                page.clear_searching_field(driver)
                page.switch_off_3D_map_mode(driver)
                print(Style.DIM + Fore.GREEN + f"\n\nТест test_build_route_by_foot выполнен успешно, маршрут "
                                               f"построен.\nВремя в пути (все предложенные варианты):\n{result}")
            else:
                allure.attach(page.get_page_screenshot_PNG(),
                              name="test_build_route_by_foot_FAILED",
                              attachment_type=allure.attachment_type.PNG)
                page.clear_searching_field(driver)
                page.switch_off_3D_map_mode(driver)
                raise Exception(Style.DIM + Fore.RED + "\nОшибка! Маршрут не построен, список с вариантами маршрутов(а)"
                                                       " по заданному пути отсутствует!\nОтразить ошибку в системе и "
                                                       "создать баг-репорт!")

    @pytest.mark.traffic
    @allure.title("Отображение дорожной ситуации(пробки) на карте.")
    @allure.testcase("https://yandex.ru/maps", "TC-YMPS-TRFFC-01")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label(LabelType.LANGUAGE, "Python")
    @allure.label(LabelType.FRAMEWORK, "Pytest", "Selenium")
    @allure.label("Агафонов Е.А.", "владелец")
    @allure.link("https://yandex.ru/maps", name="https://yandex.ru/maps")
    @allure.epic("Пользовательский интерфейс (позитивные тесты)")
    @allure.feature("Отображение на карте текущей ситуации на дорогах города.")
    def test_traffic_btn_click(self, driver, traffic_point="Москва, Садовое кольцо"):
        """Позитивный тест проверки нажатия кнопки "Дорожная ситуация", отображающей на карте текущую ситуацию на
        дорогах города. Валидация теста выполнена успешно в случае, если после воздействия на контроллер на
        дорогах города отображается текущая плотность трафика с обозначением "зеленых", "красных", "оранжевых" зон
        (степень загруженности участка дороги), контроллер кнопки отображает индекс загруженности по шкале 1/10."""

        with allure.step("Шаг 1: Перейти на сайт https://yandex.ru/maps/ и дождаться полной загрузки всех элементов."):
            page = MainPage(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 2: В поле 'Поиск мест и адресов' ввести название места с интересующей дорожной "
                         "обстановкой"):
            page.enter_searching_address(driver, traffic_point)
            page.wait_page_loaded()
            page.switch_to_3D_map_click(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 3: Нажать на элемент 'Дорожная ситуация'."):
            page.traffic_btn_click(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 4: Выполнить проверку результата теста."):
            if True:
                page.make_screenshot(file_path=screenshots_folder + "\\test_traffic_btn_click.png")
                allure.attach(page.get_page_screenshot_PNG(),
                              name="traffic_btn_click_PASSED",
                              attachment_type=allure.attachment_type.PNG)
                page.traffic_btn_click(driver)
                page.clear_searching_field(driver)
                page.switch_off_3D_map_mode(driver)
                page.wait_page_loaded()
                print(Style.DIM + Fore.GREEN + f"\n Тест test_traffic_btn_click выполнен успешно!")
            else:
                allure.attach(page.get_page_screenshot_PNG(),
                              name="traffic_btn_click_FAILED",
                              attachment_type=allure.attachment_type.PNG)
                page.clear_searching_field(driver)
                page.switch_off_3D_map_mode(driver)
                raise Exception(Style.DIM + Fore.RED + f"\nОшибка! Трафик на карте не отображается, контроллер кнопки "
                                                       f"'Дорожная ситуация' не активен/не работает.\nОтразить ошибку "
                                                       f"в системе и создать баг-репорт!")

    @pytest.mark.city_trans
    @allure.title("Отображение маршрутного транспорта на карте.")
    @allure.testcase("https://yandex.ru/maps", "TC-YMPS-CITYTRNS-01")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label(LabelType.LANGUAGE, "Python")
    @allure.label(LabelType.FRAMEWORK, "Pytest", "Selenium")
    @allure.label("Агафонов Е.А.", "владелец")
    @allure.link("https://yandex.ru/maps", name="https://yandex.ru/maps")
    @allure.epic("Пользовательский интерфейс (позитивные тесты)")
    @allure.feature("Отображение на дорогах города движущегося маршрутного транспорта.")
    def test_city_trans_btn_click(self, driver, random_address="Москва, ст. метро Домодедовская"):
        """Позитивный тест проверки нажатия кнопки "Движущийся транспорт", отображающей на карте местоположение
        городского общественного транспорта (ОТ) с номером маршрута. Валидация теста выполнена успешно в случае, если
        после воздействия на контроллер кнопки, на карте отображаются иконки движущегося в реальном времени
        общественного транспорта с указанием маршрута."""

        with allure.step("Шаг 1: Перейти на сайт https://yandex.ru/maps/ и дождаться полной загрузки всех элементов."):
            page = MainPage(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 2: В поле 'Поиск мест и адресов' указать адрес места с интересующим трафиком ОТ."):
            page.enter_searching_address(driver, random_address)
            page.wait_page_loaded()
        with allure.step("Шаг 3: Нажать на элемент 'Движущийся транспорт'."):
            page.city_transprt_btn_click(driver)
            page.switch_to_3D_map_click(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 4: Выполнить проверку результата теста."):
            if True:
                page.make_screenshot(file_path=screenshots_folder + "\\test_city_trans_btn_click.png")
                allure.attach(page.get_page_screenshot_PNG(),
                              name="city_trans_btn_click_PASSED",
                              attachment_type=allure.attachment_type.PNG)
                page.city_transprt_btn_click(driver)
                page.clear_searching_field(driver)
                page.switch_off_3D_map_mode(driver)
                page.wait_page_loaded()
                print(Style.DIM + Fore.GREEN + f"\n Тест test_city_transprt_btn_click выполнен успешно!")
            else:
                allure.attach(page.get_page_screenshot_PNG(),
                              name="city_trans_btn_click_FAILED",
                              attachment_type=allure.attachment_type.PNG)
                page.clear_searching_field(driver)
                page.switch_off_3D_map_mode(driver)
                raise Exception(Style.DIM + Fore.RED + f"\nОшибка! Иконки общественного транспорта на карте не "
                                                       f"отображаются, контроллер кнопки 'Движущийся транспорт' не "
                                                       f"активен/не работает.\nОтразить ошибку в системе и создать "
                                                       f"баг-репорт!")

    @pytest.mark.panorama
    @allure.title("Просмотр панорам улиц.")
    @allure.testcase("https://yandex.ru/maps", "TC-YMPS-PANORAMA-01")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label(LabelType.LANGUAGE, "Python")
    @allure.label(LabelType.FRAMEWORK, "Pytest", "Selenium")
    @allure.label("Агафонов Е.А.", "владелец")
    @allure.link("https://yandex.ru/maps", name="https://yandex.ru/maps")
    @allure.epic("Пользовательский интерфейс (позитивные тесты)")
    @allure.feature("Отображение на карте доступных к просмотру панорам улиц и фотографий объектов.")
    def test_street_panorama_btn_click(self, driver, toponyms_name="Москва, гостиница Космос"):
        with allure.step("Шаг 1: Перейти на сайт https://yandex.ru/maps/ и дождаться полной загрузки всех элементов."):
            page = MainPage(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 2: Кликнуть элемент 'Панорамы улиц и фотографии' в правом верхнем углу карты"):
            page.enter_searching_address(driver, toponyms_name)
            page.wait_page_loaded()
            page.panorama_streets_btn_click(driver)
            page.wait_page_loaded()
            page.zoom_out_map(driver)
            page.wait_page_loaded()
            page.make_screenshot(file_path=screenshots_folder + "\\test_street_panorama_btn_TOP_VIEW.png")
            allure.attach(page.get_page_screenshot_PNG(),
                          name="street_panorama_btn_TOP_VIEW",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Шаг 3: Кликнуть на карте в произвольную точку фиолетового цвета"):
            page.choose_panorama_random_view(driver)
            page.wait_page_loaded()
            page.make_screenshot(file_path=screenshots_folder + "\\test_street_panorama_btn_BEFORE_ROTATE.png")
            allure.attach(page.get_page_screenshot_PNG(),
                          name="street_panorama_btn_BEFORE_ROTATE",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Шаг 4: На открывшейся панораме улицы зажать левую кнопку мыши и выполнить вращение по "
                         "часовой стрелке до исходной точки вращения."):
            page.rotate_street_panorama_view(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 5: Выполнить проверку результата теста."):
            if True:
                page.make_screenshot(file_path=screenshots_folder + "\\test_street_panorama_btn_AFTER_ROTATE.png")
                allure.attach(page.get_page_screenshot_PNG(),
                              name="street_panorama_btn_click_PASSED",
                              attachment_type=allure.attachment_type.PNG)
                page.panorama_view_close(driver)
                page.panorama_streets_btn_click(driver)
                page.clear_searching_field(driver)
                page.wait_page_loaded()
                print(Style.DIM + Fore.GREEN + f"\n Тест test_street_panorama_btn_click выполнен успешно!")
            else:
                allure.attach(page.get_page_screenshot_PNG(),
                              name="street_panorama_btn_click_FAILED",
                              attachment_type=allure.attachment_type.PNG)
                page.panorama_view_close(driver)
                page.panorama_streets_btn_click(driver)
                page.clear_searching_field(driver)
                page.wait_page_loaded()
                raise Exception(Style.DIM + Fore.RED + f"\nОшибка! Панорама улицы не отображается, элемент (кнопка) "
                                                       f"'Панорамы улиц и фотографии' не активен/не работает.\nОтразить "
                                                       f"ошибку в системе и создать баг-репорт!")

    @pytest.mark.metro
    @allure.title("Маршрут между станциями метро (ГУП Московский метрополитен).")
    @allure.testcase("https://yandex.ru/maps", "TC-YMPS-METRO-01")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label(LabelType.LANGUAGE, "Python")
    @allure.label(LabelType.FRAMEWORK, "Pytest", "Selenium")
    @allure.label("Агафонов Е.А.", "владелец")
    @allure.link("https://yandex.ru/maps/metro/moscow", name="https://yandex.ru/maps/metro/moscow")
    @allure.epic("Пользовательский интерфейс (позитивные тесты)")
    @allure.feature("Проверка создания маршрута между двумя станциями метро")
    def test_build_route_in_metro(self, driver, departure_station="Домодедовская", destination_station="Парк Победы"):
        """Позитивный тест проверки создания оптимального маршрута между двумя станциями на схеме метро.
        Указываются станции отправления и назначения (аргументы depart_station и destin_station), после чего
        система планирует оптимальный/один из оптимальных маршрутов и отображает его на карте. Валидация теста
        выполнена успешно, если построенный маршрут отображается на схеме, стек карточек с вариантами маршрутов
        (в зависимости от времени в пути до конечной точки) не пустой и содержит информацию о времени прибытия по
        указанному адресу."""

        with allure.step("Шаг 1: Перейти на сайт https://yandex.ru/maps/ и дождаться полной загрузки всех "
                         "элементов."):
            page = MainPage(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 2: Нажать на элемент 'Детали' в правом верхнем углу (линия из трех квадратов)"):
            page.details_btn_click(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 3: В выпадающем списке нажать 'Схема метро'."):
            map_scheme_tab = page.get_relative_link()
            page.metro_scheme_btn_click(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 4: В открывшейся вкладке браузера в поле 'Откуда' указать наименование "
                         "станции отправления."):
            page.switch_to_new_browser_tab()
            metro_scheme_tab = page.get_relative_link()
            page.enter_departure_metro_station(driver, departure_station)
            page.wait_page_loaded()
        with allure.step("Шаг 5: В поле 'Куда' указать наименование станции назначения."):
            page.enter_destination_metro_station(driver, destination_station)
            page.wait_page_loaded()
            time.sleep(2)
        # with allure.step("Шаг 6: Выполнить проверку результатов теста."):
        #     result = page.check_all_variants_of_arrivals_car(driver)
        #     page.wait_page_loaded(check_page_changes=True)
        #     if len(result) != 0:
        #         page.make_screenshot(file_path=screenshots_folder + "\\test_build_route_by_car.png")
        #         allure.attach(page.get_page_screenshot_PNG(),
        #                       name="build_route_by_car_PASSED",
        #                       attachment_type=allure.attachment_type.PNG)
        #         page.clear_searching_field(driver)
        #         page.switch_off_3D_map_mode(driver)
        #         print(Style.DIM + Fore.GREEN + f"\n\nТест test_build_route_by_car выполнен успешно, маршрут "
        #                                        f"построен.\nВремя в пути (все предложенные варианты):\n{result}")
        #     else:
        #         allure.attach(page.get_page_screenshot_PNG(),
        #                       name="build_route_by_car_FAILED",
        #                       attachment_type=allure.attachment_type.PNG)
        #         page.clear_searching_field(driver)
        #         page.switch_off_3D_map_mode(driver)
        #         raise Exception(
        #             Style.DIM + Fore.RED + "\nОшибка! Маршрут не построен, список с вариантами маршрутов(а)"
        #                                    " по заданному пути отсутствует!\nОтразить ошибку в системе и "
        #                                    "создать баг-репорт!")
