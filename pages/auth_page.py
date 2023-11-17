import os
from pages.base_page import BasePage
from pages.locators import AuthLocators


class AuthPage(BasePage):
    """Класс с атрибутами и методами для управления элементами страницы авторизации пользователя по адресу -
    https://petfriends.skillfactory.ru/login в рамках проектирования UI-тестов по паттерну PageObjectModel."""

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)

        url = os.getenv("LOGIN_URL") or "https://petfriends.skillfactory.ru/login"
        driver.get(url)
        self.email = driver.find_element(*AuthLocators.AUTH_EMAIL)
        self.passw = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_pass(self, value):
        self.passw.send_keys(value)

    def btn_click(self):
        self.btn.click()

    def check_allert_msg(self, driver):
        msg = driver.find_element(*AuthLocators.AUTH_ALERT_MSG).text
        return msg
