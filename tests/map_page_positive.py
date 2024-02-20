import pytest
from pages.main_page import MainPage
from settings import *
from colorama import Fore, Style
import allure
from allure_commons.types import LabelType


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
            page.decrease_map_size(driver, amount="high")
            page.decrease_map_size(driver)
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
        Контроль теста определяется по скриншотам, сделанным в начальный момент, в момент увеличения и в момент
        уменьшения размера карты."""

        with allure.step("Шаг 1: Перейти на сайт https://yandex.ru/maps/ и дождаться полной загрузки всех элементов."):
            page = MainPage(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 2: Кликнуть элемент 'Отдалить' 2(два) раза"):
            page.enter_searching_address(driver, random_place)
            page.wait_page_loaded()
            page.decrease_map_size(driver, amount="medium")
            page.wait_page_loaded(check_page_changes=True)
            page.make_screenshot(file_path=screenshots_folder + "\\test_change_map_size_decreased.png")
            allure.attach(page.get_page_screenshot_PNG(),
                          name="change_map_size_btn_decrsd_x_2",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Шаг 3: Кликнуть элемент 'Приблизить' 3(три) раза"):
            page.increase_map_size(driver, amount="medium")
            page.wait_page_loaded()
            page.make_screenshot(file_path=screenshots_folder + "\\test_change_map_size_increased.png")
            allure.attach(page.get_page_screenshot_PNG(),
                          name="change_map_size_btn_incrs_x_3",
                          attachment_type=allure.attachment_type.PNG)
            page.clear_searching_field(driver)
        with allure.step("Шаг 4: Проверка результатов теста."):
            if True:
                print("\nВалидация теста test_incrise_decrise_map_size_btn выполнена успешно!")
            else:
                raise Exception("\nОшибка! Проверьте корректность локаторов элементов 'Приблизить', 'Отдалить'. Иначе "
                                "отразить ошибку в системе и создать баг-репорт.")

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
            page.increase_map_size(driver)
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
            page.wait_page_loaded()
        with allure.step("Шаг 6: Выполнить проверку результатов теста."):
            result = page.check_all_variants_of_arrivals_city(driver)
            if len(result) != 0:
                page.make_screenshot(file_path=screenshots_folder + "\\test_build_route_by_car.png")
                allure.attach(page.get_page_screenshot_PNG(),
                              name="build_route_by_car_PASSED",
                              attachment_type=allure.attachment_type.PNG)
                page.clear_searching_field(driver)
                page.switch_off_3D_map_mode(driver)
                print(Style.DIM + Fore.GREEN + f"\n\nТест test_build_route_by_city_trnsprt выполнен успешно, маршрут "
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
            result = page.traffic_btn_click(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 4: Выполнить проверку результата теста."):
            if result:
                page.make_screenshot(file_path=screenshots_folder + "\\test_traffic_btn_click.png")
                allure.attach(page.get_page_screenshot_PNG(),
                              name="traffic_btn_click_PASSED",
                              attachment_type=allure.attachment_type.PNG)
                page.clear_searching_field(driver)
                page.switch_off_3D_map_mode(driver)
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
            result = page.city_transprt_btn_click(driver)
            page.switch_to_3D_map_click(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 4: Выполнить проверку результата теста."):
            if result:
                page.make_screenshot(file_path=screenshots_folder + "\\test_city_trans_btn_click.png")
                allure.attach(page.get_page_screenshot_PNG(),
                              name="city_trans_btn_click_PASSED",
                              attachment_type=allure.attachment_type.PNG)
                page.clear_searching_field(driver)
                page.switch_off_3D_map_mode(driver)
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
