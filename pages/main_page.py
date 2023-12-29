from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from pages.base_page import BasePage
from pages.locators import MapPageLocators
import os


class MainPage(BasePage):
    """Наследованный класс с атрибутами и методами для управления элементами на главной странице веб-приложения
    "Яндекс.Карты" (поисково-информационная картографическая служба Яндекса) в рамках проектирования UI-тестов по
    паттерну Page Object Model."""

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

        self.current_geo_btn = driver.find_element(*MapPageLocators.MAP_MY_GEOLOC_BTN)
        self.incrise_view_size = driver.find_element(*MapPageLocators.MAP_INCRISE_VIEW_SIZE)
        self.decrease_view_size = driver.find_element(*MapPageLocators.MAP_DECREASE_VIEW_SIZE)

    def enter_searching_address(self, driver, value: str):
        """Поиск топонима на веб-платформе Яндекс.Карты. Передает в поле поиска название(адрес) искомого объекта и
        подтверждает действие."""

        address = driver.find_element(*MapPageLocators.MAP_SEARCH_FIELD)
        ActionChains(driver).send_keys_to_element(address, value).pause(2).send_keys(Keys.DOWN).send_keys(Keys.ENTER) \
            .perform()

    def my_current_geoloc_btn_click(self):
        """Осуществляет нажатие кнопки 'Моё местоположение' на веб-карте."""
        self.current_geo_btn.click()

    def incrise_map_size(self, amount="low"):
        """Осуществляет нажатие кнопки 'Приблизить' на карте. Для выбора кратности увеличения масштаба карты можно
        задать значение аргумента amount равным: 'low', 'medium' или 'high'."""
        if amount == "low":
            self.incrise_view_size.click()
        elif amount == "medium":
            self.incrise_view_size.click()
            self.incrise_view_size.click()
        elif amount == "high":
            self.incrise_view_size.click()
            self.incrise_view_size.click()
            self.incrise_view_size.click()
        else:
            raise Exception(
                f"\nОшибка! Методу incrise_map_size() задано некорректное значение параметра amount={amount}!\n"
                f"Доступные значения:"
                f"\n'low', 'medium' или 'high'")

    def decrease_map_size(self, amount="low"):
        """Осуществляет нажатие кнопки 'Отдалить' на карте. Для выбора кратности уменьшения масштаба карты можно задать
        значение аргумента amount равным: 'low', 'medium' или 'high'."""

        if amount == "low":
            self.decrease_view_size.click()
        elif amount == "medium":
            self.decrease_view_size.click()
            self.decrease_view_size.click()
        elif amount == "high":
            self.decrease_view_size.click()
            self.decrease_view_size.click()
            self.decrease_view_size.click()
        else:
            raise Exception(
                f"\nОшибка! Методу dicrise_map_size() задано некорректное значение параметра amount={amount}!\n"
                f"Доступные значения:"
                f"\n'low', 'medium' или 'high'")

    @staticmethod
    def get_toponym_descript(driver):
        """Метод для получения(парсинга) названия топонима, отображаемого системой после его поиска на карте. Необходим
        для валидации теста."""

        parsed_toponym = driver.find_element(*MapPageLocators.MAP_TOPONYM_DESCRIPTION).text
        return parsed_toponym

    def switch_to_3D_map_click(self, driver):
        """Осуществляет нажатие кнопки 'Наклонить карту' для перехода в режим изометрического(3D) отображения карты."""

        map_3D_btn = driver.find_element(*MapPageLocators.MAP_SWITCH_TO_3D_MAP_BTN)
        map_3D_btn.click()

    def build_route_btn_click(self, driver):
        """Осуществляет нажатие кнопки 'Маршруты' для создания пользовательского маршрута на карте."""

        build_route_btn = driver.find_element(*MapPageLocators.MAP_BUILD_ROUTE_BTN)
        build_route_btn.click()

    def enter_departure_address(self, driver, value):
        """Создание начальной точки маршрута. Через аргумент value передает в поле ввода на карте название(адрес) точки
        отправления и подтверждает действие."""

        dep_address = driver.find_element(*MapPageLocators.MAP_DEPARTURES_ADDRESS_FIELD)
        ActionChains(driver).send_keys_to_element(dep_address, value).pause(2).send_keys(Keys.DOWN).send_keys \
            (Keys.ENTER).perform()

    def enter_destination_address(self, driver, value):
        """Создание конечной точки маршрута. Через аргумент value передает в поле ввода на карте название(адрес)
        места назначения и подтверждает действие."""

        dest_address = driver.find_element(*MapPageLocators.MAP_DESTINATION_ADDRESS_FIELD)
        ActionChains(driver).send_keys_to_element(dest_address, value).pause(2).send_keys(Keys.DOWN).send_keys \
            (Keys.ENTER).perform()

    def check_all_variants_of_arrivals(self, driver):
        """Метод для получения(парсинга) информации о продолжительности маршрута(ов), сформированного(ых) системой.
        Формирует список расчетного времени по всем вариантам маршрутов. Необходим для валидации теста."""

        all_arrivals = driver.find_elements(*MapPageLocators.MAP_EXPECTED_TIME_OF_ARRIVAL)
        list_of_arrivals = []
        for i in range(len(all_arrivals)):
            arrival_time = all_arrivals[i].text
            list_of_arrivals.append(arrival_time)
        return list_of_arrivals

    def traffic_btn_click(self, driver):
        """Осуществляет нажатие кнопки 'Дорожная ситуация' для отображения на карте уровня загруженности дорог(пробок) и
        дорожной обстановки."""

        traffic = driver.find_element(*MapPageLocators.MAP_TRAFFIC_BTN)
        traffic.click()
        return traffic

    def city_transprt_btn_click(self, driver):
        """Осуществляет нажатие кнопки 'Движущийся транспорт' для отображения на карте движущихся единиц общественного
        транспорта с указанными маршрутными номерами."""

        transport = driver.find_element(*MapPageLocators.MAP_CITY_TRANSPORT)
        transport.click()
        return transport
