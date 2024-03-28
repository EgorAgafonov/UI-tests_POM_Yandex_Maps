import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver import Keys
from pages.base_page import BasePage
from pages.locators import MapPageLocators
from tkinter import *


class MainPage(BasePage):
    """Наследованный класс с атрибутами и методами для управления элементами на главной странице веб-приложения
    "Яндекс.Карты" (поисково-информационная картографическая служба Яндекса) в рамках проектирования UI-тестов по
    паттерну Page Object Model."""

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def enter_searching_address(self, driver, value: str):
        """Поиск топонима на веб-платформе Яндекс.Карты. Передает в поле поиска название(адрес) искомого объекта и
        подтверждает действие."""

        address_field = driver.find_element(*MapPageLocators.MAP_SEARCH_FIELD)
        ActionChains(driver).send_keys_to_element(address_field, value).pause(3).send_keys(Keys.DOWN)\
            .send_keys(Keys.ENTER) \
            .perform()

    def clear_searching_field(self, driver):
        """Метод очищает поле поиска от текста после ввода названия искомого топонима посредством воздействия на элемент
         'Закрыть' (крестик)."""

        clear_search_field = driver.find_element(*MapPageLocators.MAP_CLEAR_FIELD_BTN)
        clear_search_field.click()

    def my_current_geoloc_btn_click(self, driver):
        """Осуществляет нажатие кнопки 'Моё местоположение' на веб-карте."""

        curent_geoloc = driver.find_element(*MapPageLocators.MAP_MY_GEOLOC_BTN)
        curent_geoloc.click()

    @staticmethod
    def get_current_geoloc_name(driver):
        """Метод для получения(парсинга) названия места текущей геолокации пользователя. Необходим для валидации
        теста."""

        geoloc_name = driver.find_element(*MapPageLocators.MAP_MY_GEOLOC_NAME).text
        return geoloc_name

    def zoom_in_map(self, driver, amount="low"):
        """Осуществляет нажатие кнопки 'Приблизить' на карте. Для выбора кратности увеличения масштаба карты можно
        задать значение аргумента amount равным: 'low', 'medium' или 'high'."""

        increase_btn = driver.find_element(*MapPageLocators.MAP_INCREASE_VIEW_SIZE)

        if amount == "low":
            ActionChains(driver).click(increase_btn).pause(0.5).perform()
        elif amount == "medium":
            ActionChains(driver).click(increase_btn).pause(0.5).click(increase_btn).pause(0.5).perform()
        elif amount == "high":
            ActionChains(driver).click(increase_btn).pause(0.5).click(increase_btn).pause(0.5)\
                                .click(increase_btn).pause(0.5).perform()
        else:
            raise Exception(
                f"\nОшибка! Методу incrise_map_size() задано некорректное значение параметра amount={amount}!\n"
                f"Доступные значения:"
                f"\n'low', 'medium' или 'high'")

    def zoom_out_map(self, driver, amount="low"):
        """Осуществляет нажатие кнопки 'Отдалить' на карте. Для выбора кратности уменьшения масштаба карты можно задать
        значение аргумента amount равным: 'low', 'medium' или 'high'."""

        decrease_btn = driver.find_element(*MapPageLocators.MAP_DECREASE_VIEW_SIZE)

        if amount == "low":
            ActionChains(driver).click(decrease_btn).pause(0.5).perform()
        elif amount == "medium":
            ActionChains(driver).click(decrease_btn).pause(0.5).click(decrease_btn).pause(0.5).perform()
        elif amount == "high":
            ActionChains(driver).click(decrease_btn).pause(0.5).click(decrease_btn).pause(0.5)\
                                .click(decrease_btn).pause(0.5).perform()
        else:
            raise ValueError(
                f"\nОшибка! Методу dicrise_map_size() задано некорректное значение параметра amount={amount}!\n"
                f"Доступные значения:"
                f"\n'low', 'medium' или 'high'")

    @staticmethod
    def choose_map_layers_btn_click(driver):
        map_layers = driver.find_element(*MapPageLocators.MAP_CHOOSE_MODE_VIEW)
        map_layers.click()

    @staticmethod
    def choose_scheme_mode_btn_click(driver):
        scheme_mode = driver.find_element(*MapPageLocators.MAP_CHOOSE_SCHEME_VIEW)
        scheme_mode.click()

    @staticmethod
    def choose_sputnik_mode_btn_click(driver):
        sputnik_mode = driver.find_element(*MapPageLocators.MAP_CHOOSE_SPUTNIK_VIEW)
        sputnik_mode.click()

    @staticmethod
    def choose_hybrid_mode_btn_click(driver):
        hybrid_mode = driver.find_element(*MapPageLocators.MAP_CHOOSE_HYBRID_VIEW)
        hybrid_mode.click()

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

    def switch_off_3D_map_mode(self, driver):
        """Осуществляет возврат из режима изометрического отображения карты(3D) обратно в 2D("вид сверху")."""

        map_3D_btn_off = driver.find_element(*MapPageLocators.MAP_SWITCH_OFF_3D_MAP_BTN)
        map_3D_btn_off.click()

    def build_route_btn_click(self, driver):
        """Осуществляет нажатие кнопки 'Маршруты' для создания пользовательского маршрута на карте."""

        build_route_btn = driver.find_element(*MapPageLocators.MAP_BUILD_ROUTE_BTN)
        build_route_btn.click()

    def route_by_car_btn_click(self, driver):
        """Осуществляет нажатие(выбор) элемента 'На автомобиле' для создания автомобильного маршрута на карте."""

        car_btn = driver.find_element(*MapPageLocators.MAP_ROUTE_BY_CAR_BTN)
        car_btn.click()

    def route_by_trnsprt_btn_click(self, driver):
        """Осуществляет нажатие(выбор) элемента 'На общественном транспорте' для создания маршрута с использованием
        общественного транспорта."""

        city_trnsprt_btn = driver.find_element(*MapPageLocators.MAP_ROUTE_BY_CITY_TRANSPORT_BTN)
        city_trnsprt_btn.click()

    def route_by_foot_btn_click(self, driver):
        """Осуществляет нажатие(выбор) элемента 'Пешком' для создания пешего маршрута."""

        walking_btn = driver.find_element(*MapPageLocators.MAP_ROUTE_BY_WALKING_BTN)
        walking_btn.click()

    def enter_departure_address(self, driver, value):
        """Создание начальной точки маршрута. Через аргумент value передает в поле ввода на карте название(адрес) точки
        отправления и подтверждает действие."""

        dep_address = driver.find_element(*MapPageLocators.MAP_DEPARTURES_ADDRESS_FIELD)
        ActionChains(driver).send_keys_to_element(dep_address, value).pause(3).send_keys(Keys.DOWN).send_keys \
            (Keys.ENTER).perform()

    def enter_destination_address(self, driver, value):
        """Создание конечной точки маршрута. Через аргумент value передает в поле ввода на карте название(адрес)
        места назначения и подтверждает действие."""

        dest_address = driver.find_element(*MapPageLocators.MAP_DESTINATION_ADDRESS_FIELD)
        ActionChains(driver).send_keys_to_element(dest_address, value).pause(3).send_keys(Keys.DOWN)\
            .send_keys(Keys.ENTER).perform()

    def check_all_variants_of_arrivals_car(self, driver):
        """Метод для получения(парсинга) информации о продолжительности маршрута(ов) на автомобиле, сформированного(ых)
        системой. Формирует список расчетного времени по всем вариантам маршрутов. Необходим для валидации теста."""

        all_arrivals = driver.find_elements(*MapPageLocators.MAP_EXPECTED_TIME_OF_ARRIVAL_CAR)
        list_of_arrivals = []
        for i in range(len(all_arrivals)):
            arrival_time = all_arrivals[i].text
            list_of_arrivals.append(arrival_time)
        return list_of_arrivals

    def check_all_variants_of_arrivals_city(self, driver) -> list:
        """Метод для получения(парсинга) информации о продолжительности маршрута(ов) на общественном транспорте,
        сформированного(ых) системой. Формирует список расчетного времени по 3 вариантам маршрутов. Необходим для
        валидации теста."""

        all_arrivals = driver.find_elements(*MapPageLocators.MAP_EXPECTED_TIME_OF_ARRIVAL_CITY_TRNSPRT)
        list_of_arrivals = []
        for i in range(len(all_arrivals)):
            arrival_time = all_arrivals[i].text
            list_of_arrivals.append(arrival_time)
        return list_of_arrivals

    def check_all_variants_time_by_foot(self, driver) -> list:
        """Метод для получения(парсинга) информации о продолжительности маршрута(ов) для пешей прогулки,
        сформированного(ых) системой. Формирует список расчетного времени по 3 вариантам маршрутов. Необходим для
        валидации теста."""

        all_variants = driver.find_elements(*MapPageLocators.MAP_TRAVEL_TIME_BY_FOOT)
        list_of_variants = []
        for i in range(len(all_variants)):
            variant = all_variants[i].text
            list_of_variants.append(variant)
        return list_of_variants

    def check_current_scale_line_value(self, driver):
        """Метод для получения(парсинга) информации о текущем масштабе отображения карты. Необходим для валидации
        теста."""

        scale_line = driver.find_element(*MapPageLocators.MAP_SCALE_LINE)
        result = scale_line.text
        return result

    def traffic_btn_click(self, driver):
        """Осуществляет нажатие кнопки 'Дорожная ситуация' для отображения на карте уровня загруженности дорог(пробок) и
        дорожной обстановки."""

        traffic = driver.find_element(*MapPageLocators.MAP_TRAFFIC_BTN)
        traffic.click()

    def city_transprt_btn_click(self, driver):
        """Осуществляет нажатие кнопки 'Движущийся транспорт' для отображения на карте движущихся единиц общественного
        транспорта с указанными маршрутными номерами."""

        transport = driver.find_element(*MapPageLocators.MAP_CITY_TRANSPORT)
        transport.click()

    @staticmethod
    def panorama_streets_btn_click(driver):
        """Осуществляет нажатие кнопки 'Панорама улиц и фотографии' для отображения на карте доступных для просмотра
        панорам улиц и фотографий."""

        panorama_btn = driver.find_element(*MapPageLocators.MAP_STREET_PANORAMA_VIEW)
        panorama_btn.click()

    @staticmethod
    def choose_panorama_random_view(driver):
        """Метод для проверки работы функции отображения панорамы улицы по выбраной на карте точке. Перемещает курсор
        мыши в центральную область экрана (считает текущие установки разрешения экрана) и
        осуществляет нажатие левой кнопкой мыши для перехода в режим отображения статической панорамы улицы.
        ВАЖНО: Данный метод необходимо использовать только в активированном режиме 'Панорамы улиц и фотографии'. Не
        зависит от разрешения экрана, установленного в текущей тестовой среде."""

        x = (Tk().winfo_screenwidth() // 2) + 100
        y = Tk().winfo_screenheight() // 2
        action = ActionBuilder(driver)
        action.pointer_action.move_to_location(x, y).click()
        action.perform()

    @staticmethod
    def rotate_street_panorama_view(driver):
        """Метод для вращения статического изображения уличной панорамы вокруг наблюдателя. Необходим для валидации
        тест-кейса test_street_panorama_btn_click."""

        x = (Tk().winfo_screenwidth() // 2)
        y = Tk().winfo_screenheight() // 2
        x_step = -(x // 2)
        y_step = 0
        action = ActionBuilder(driver)
        action.pointer_action.move_to_location(x, y).click_and_hold().pause(1).move_by(x_step, y_step).release()\
            .move_to_location(x, y).click_and_hold().pause(0.5).move_by(x_step, y_step).release()\
            .move_to_location(x, y).click_and_hold().pause(0.5).move_by(x_step, y_step).release()\
            .move_to_location(x, y).click_and_hold().pause(0.5).move_by(x_step, y_step).release()\
            .move_to_location(x, y).click_and_hold().pause(0.5).move_by(x_step, y_step).release()\
            .move_to_location(x, y).click_and_hold().pause(0.5).move_by(x_step, y_step).release()\
            .move_to_location(x, y).click_and_hold().pause(0.5).move_by(x_step, y_step).release()
        action.perform()

    @staticmethod
    def panorama_view_close(driver):
        """Осуществляет нажатие кнопки 'Закрыть' на экране текущей панорамы улицы."""

        panorama_close_btn = driver.find_element(*MapPageLocators.MAP_CLOSE_PANORAMA_VIEW)
        panorama_close_btn.click()

    @staticmethod
    def details_btn_click(driver):
        """Осуществляет вызов выпадающего меню 'Детали' на экране карты для доступа к опциональным функциям сервиса."""

        details_btn = driver.find_element(*MapPageLocators.MAP_DETAILS_MENU)
        details_btn.click()

    @staticmethod
    def metro_scheme_btn_click(driver):
        """Осуществляет нажатие элемента 'Схема метро' в выпадающем меню 'Детали'."""

        metro_scheme = driver.find_element(*MapPageLocators.MAP_METRO_SCHEME)
        metro_scheme.click()

    @staticmethod
    def enter_departure_metro_station(driver, value: str):
        """Метод для определения станции отправления на схеме метро. Параметр value указывает строчное наименование
        станции метро и передает его в соответствующее поле ввода на веб-странице."""

        departure_station = driver.find_element(*MapPageLocators.MAP_DEPARTURE_METRO_STATION_FIELD)
        ActionChains(driver).send_keys_to_element(departure_station, value).pause(1).send_keys(Keys.DOWN)\
            .send_keys(Keys.ENTER).perform()

    @staticmethod
    def enter_destination_metro_station(driver, value: str):
        """Метод для определения станции назначения на схеме метро. Аналогичен работе метода enter_departure_metro_
        station, но передает в поле для ввода наименование станции назначения."""

        departure_station = driver.find_element(*MapPageLocators.MAP_DESTINATION_METRO_STATION_FIELD)
        ActionChains(driver).send_keys_to_element(departure_station, value).pause(1).send_keys(Keys.DOWN)\
            .send_keys(Keys.ENTER).perform()

    @staticmethod
    def check_all_variants_of_metro_rides(driver):
        """Метод для получения(парсинга) информации о всех(либо одном) возможных вариантах поездки между указанными
        станциям метро, сформированных системой. Возвращает список с указанной длительностью поездки по каждому(либо
        одному)предложенному варианту. Необходим для валидации теста."""

        all_metro_rides = driver.find_elements(*MapPageLocators.MAP_METRO_RIDES_DURATION)
        list_of_rides_duration = []
        for i in range(len(all_metro_rides)):
            duration_time = all_metro_rides[i].text
            list_of_rides_duration.append(duration_time)
        return list_of_rides_duration
