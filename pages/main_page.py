from pages.base_page import BasePage
from pages.locators import MainPageLocators
import os


class MainPage(BasePage):
    """Класс с атрибутами и методами для управления элементами главной страницы https://www.mvideo.ru/
     в рамках проектирования UI-тестов по паттерну Page Object Model."""

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

        self.search_field = driver.find_element(*MainPageLocators.MAIN_SEARCH_FIELD)
        self.submit_search_btn = driver.find_element(*MainPageLocators.MAIN_SUBMIT_SEARCH_BTN)
        self.catalog_btn = driver.find_element(*MainPageLocators.MAIN_CATALOG_BTN)

    def enter_products_name(self, value):
        self.search_field.send_keys(value)

    def clear_search_field(self):
        self.search_field.clear()

    def submit_search_btn_click(self):
        self.submit_search_btn.click()

    def catalog_btn_click(self):
        self.catalog_btn.click()



    # def get_pets_quantity(self, driver):
    #     num = len(driver.find_elements(*MyPetsLocators.MY_PETS_CARDS_QUANTITY))
    #     return num

