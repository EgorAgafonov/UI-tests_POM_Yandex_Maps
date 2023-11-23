from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from pages.locators import MapPageLocators
import os


class MainPage(BasePage):
    """Класс с атрибутами и методами для управления элементами на главной странице веб-приложения "Яндекс Карты"
    (поисково-информационная картографическая служба Яндекса) в рамках проектирования UI-тестов по паттерну Page Object
    Model."""

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

        self.search_field = driver.find_element(*MapPageLocators.MAP_SEARCH_FIELD)
        self.submit_search_btn = driver.find_element(*MapPageLocators.MAP_SUBMIT_SEARCH_BTN)
        self.current_geo_btn = driver.find_element(*MapPageLocators.MAP_MY_GEOLOC_BTN)
        self.incrise_view_size = driver.find_element(*MapPageLocators.MAP_INCRISE_VIEW_SIZE)
        self.decrease_view_size = driver.find_element(*MapPageLocators.MAP_DECREASE_VIEW_SIZE)
        self.switch_to_3D_map_btn = driver.find_element(*MapPageLocators.MAP_SWITCH_TO_3D_MAP_BTN)
        self.rotate_3D_map_ring = driver.find_element(*MapPageLocators.MAP_ROTATE_RING_CONTROLLER)

    def enter_searching_address(self, value):
        self.search_field.send_keys(value)

    def clear_search_field(self):
        self.search_field.clear()

    def submit_search_btn_click(self):
        self.submit_search_btn.click()

    def my_current_geoloc_btn_click(self):
        self.current_geo_btn.click()

    def incrise_map_size(self, amount="low"):
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

    def get_toponym_descript(self, driver):
        parsed_toponym = driver.find_element(*MapPageLocators.MAP_TOPONYM_DESCRIPTION).text
        return parsed_toponym

    def switch_to_3D_map_click(self):
        self.switch_to_3D_map_btn.click()

    # def rotate_3D_map_ring(self, x_offset=-20, y_offset=0):
    #     clickable = self.rotate_3D_map_ring
    #     ActionChains(driver=self.driver) \
    #         .move_to_element_with_offset(clickable, 8, 0)\
    #         .click_and_hold(clickable) \
    #         .move_by_offset(x_offset, y_offset) \
    #         .perform()

