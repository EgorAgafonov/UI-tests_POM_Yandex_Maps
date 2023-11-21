from pages.base_page import BasePage
from pages.locators import MainPageLocators
import os


class MainPage(BasePage):
    """Класс с атрибутами и методами для управления элементами на главной странице веб-приложения "Яндекс Карты"
    (поисково-информационная картографическая служба Яндекса) в рамках проектирования UI-тестов по паттерну Page Object
    Model."""

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

        self.search_field = driver.find_element(*MainPageLocators.MAIN_SEARCH_FIELD)
        self.submit_search_btn = driver.find_element(*MainPageLocators.MAIN_SUBMIT_SEARCH_BTN)
        self.current_geo_btn = driver.find_element(*MainPageLocators.MAIN_MY_GEO_BTN)
        self.incrise_view_size = driver.find_element(*MainPageLocators.MAIN_INCRISE_VIEW_SIZE)
        self.dicrise_view_size = driver.find_element(*MainPageLocators.MAIN_DICRISE_VIEW_SIZE)

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

    def decrise_map_size(self, amount="low"):
        if amount == "low":
            self.dicrise_view_size.click()
        elif amount == "medium":
            self.dicrise_view_size.click()
            self.dicrise_view_size.click()
        elif amount == "high":
            self.dicrise_view_size.click()
            self.dicrise_view_size.click()
            self.dicrise_view_size.click()
        else:
            raise Exception(
                f"\nОшибка! Методу dicrise_map_size() задано некорректное значение параметра amount={amount}!\n"
                f"Доступные значения:"
                f"\n'low', 'medium' или 'high'")

    def get_toponym_descript(self, driver):
        parsed_toponym = driver.find_element(*MainPageLocators.MAIN_TOPONYM_DESCRIPTION).text
        return parsed_toponym


    # def get_pets_quantity(self, driver):
    #     num = len(driver.find_elements(*MyPetsLocators.MY_PETS_CARDS_QUANTITY))
    #     return num
