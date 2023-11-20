import pytest
from pages.main_page import MainPage
from settings import *
from colorama import Fore, Style
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID)))


class TestMainPagePositive:
    @pytest.mark.one
    def test_search_info_positive(self, driver):
        """Позитивный тест проверки создания карточки питомца без фото. Валидация теста выполнена успешно в случае, если
        после ввода всех необходимых данных в форму карточки, пользователь остается на страницы path = "/my_pets", а
        карточка отображается в стеке питомцев пользователя со всеми переданными данными (без фото соответственно)."""

        page = MainPage(driver)
        # time.sleep(3)
        page.clear_search_field()
        # time.sleep(3)
        page.enter_searching_info("Метро Домодедовская")
        time.sleep(3)
        page.submit_search_btn_click()
        time.sleep(3)
        page.make_screenshot()

