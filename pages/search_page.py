from pages.base_page import BasePage
from pages.locators import MyPetsLocators
import os


class MyPetsPage(BasePage):
    """Класс с атрибутами и методами для управления элементами страницы https://petfriends.skillfactory.ru/my_pets
     в рамках проектирования UI-тестов по паттерну Page Object Model."""

    def __init__(self, driver, timeout=15):
        super().__init__(driver, timeout)

        url = os.getenv("MY_PETS_URL") or "https://petfriends.skillfactory.ru/my_pets"
        driver.get(url)

        self.add_pet_btn = driver.find_element(*MyPetsLocators.MY_PETS_NEW_PET_BTN)
        self.submit_pet_btn = driver.find_element(*MyPetsLocators.MY_PETS_SUBMIT_PET_BTN)
        self.delete_pet_btn = driver.find_element(*MyPetsLocators.MY_PETS_DELETE_PET_BTN)
        self.photo = driver.find_element(*MyPetsLocators.MY_PETS_PHOTO)
        self.name = driver.find_element(*MyPetsLocators.MY_PETS_NAME)
        self.breed = driver.find_element(*MyPetsLocators.MY_PETS_BREED)
        self.age = driver.find_element(*MyPetsLocators.MY_PETS_AGE)

    def enter_photo(self, photo):
        self.photo.send_keys(photo)

    def enter_name(self, value):
        self.name.send_keys(value)

    def enter_breed(self, value):
        self.breed.send_keys(value)

    def enter_age(self, value):
        self.age.send_keys(value)

    def add_pet_btn_click(self):
        self.add_pet_btn.click()

    def submit_pet_btn_click(self):
        self.submit_pet_btn.click()

    def delete_pet_btn_click(self):
        self.delete_pet_btn.click()

    def get_pets_quantity(self, driver):
        num = len(driver.find_elements(*MyPetsLocators.MY_PETS_CARDS_QUANTITY))
        return num

