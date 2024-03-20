from urllib.parse import urlparse
from settings import screenshots_folder
from colorama import Style, Fore
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


class BasePage(object):
    """Базовый(родительский) класс веб-страницы. Определяет основные методы взаимодействия со страницами в рамках
    проектирования UI-тестов по паттерну PageObjectModel."""

    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.timeout = timeout

    def get_relative_link(self):
        """Метод для получения из URL-адреса текущей страницы значения параметра path. Необходим для валидации
        тестов при переходе на другие path-директории(эндпоинты) в тестируемом домене."""

        url = urlparse(self.driver.current_url)
        return url.path

    def get_title_of_tab(self):
        """Метод для получения названия заголовка текущей(используемой) вкладки браузера."""
        title = self.driver.title
        return title

    def get_current_tab_ID_descriptor(self) -> str:
        """Метод для получения строкового значения дескриптора(идентификационного номера) текущего окна(вкладки)
        браузера."""

        current_tab = self.driver.current_window_handle
        return current_tab

    def switch_to_new_browser_tab(self, starting_page: str):
        """Метод для перехода и работы в новом окне браузера (в новой вкладке). Для "переключения" на новую вкладку
        аргументу main_page необходимо передать строковое значение дескриптора первоначальной страницы с начала
        сессии браузера. ВАЖНО: значение дескриптора первоначальной страницы необходимо определить заранее (в начале
        теста) с помощью метода get_current_tab_ID_descriptor()."""

        for window_handle in self.driver.window_handles:
            if window_handle != starting_page:
                self.driver.switch_to.window(window_handle)
                break

    def close_current_browser_tab(self):
        """Метод для закрытия текущей вкладки браузера."""

        self.driver.close()

    def switch_back_to_main_tab(self, main_window_id: str):
        """Метод для возвращения к начальному окну сеанса. Аргумент main_window_id принимает строковое значение
        дескриптора окна - идентификационного номера окна(вкладки), с которого начался сеанс работы браузера. ВАЖНО:
        Значение дескриптора основного окна необходимо определить заранее (в начале теста) с помощью метода
        get_current_tab_ID_descriptor()"""

        self.driver.switch_to.window(main_window_id)

    def refresh_page(self):
        """Метод обновления(перезагрузки) страницы."""

        self.driver.refresh()

    def make_screenshot(self, file_path=screenshots_folder):
        """Метод сохранения изображения на экране в момент выполнения теста."""

        self.driver.save_screenshot(file_path)

    def get_page_screenshot_PNG(self) -> bytes:
        """Метод создает бинарный объект - скриншот текущей страницы в формате PNG, после чего возвращает его при
        соответствующем вызове."""

        screenshot_png = self.driver.get_screenshot_as_png()
        return screenshot_png

    def scroll_down(self, offset=0):
        """Метод прокрутки страницы вниз."""

        if offset:
            self.driver.execute_script(f'window.scrollTo(0, {offset});')
        else:
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def scroll_up(self, offset=0):
        """Метод прокрутки страницы вверх."""

        if offset:
            self.driver.execute_script(f'window.scrollTo(0, -{offset});')
        else:
            self.driver.execute_script('window.scrollTo(0, -document.body.scrollHeight);')

    def switch_to_iframe(self, iframe):
        """ Фокусировка на элементе страницы по его имени."""

        self.driver.switch_to.frame(iframe)

    def switch_out_iframe(self):
        """ Отмена фокусировки на элементе страницы по его имени."""
        self.driver.switch_to.default_content()

    def get_page_source(self):
        """Возвращает код(разметку) страницы в текстовом формате."""

        source = ''
        try:
            source = self.driver.page_source
        except:
            raise Exception(Style.DIM + Fore.RED + 'Can not get page source')

        return source

    def wait_page_loaded(self, timeout=30, check_js_complete=True, check_page_changes=False, check_images=False,
                         wait_for_element=None, wait_for_xpath_to_disappear='', sleep_time=2):

        """ Метод для реализации гибкой стратегии ожидания появления элементов страницы. Возможно задать следующее
        количество аргументов(маркеров) для определения полной загрузки:
        1) Проверка JavaScript статуса страницы;
        2) Проверка изменений в исходном коде страницы;
        3) Проверка загрузки изображений на странице (ВАЖНО: эта проверка отключена по умолчанию);
        4) Проверка загрузки конкретного элемента страницы, ожидаемого пользователем."""

        page_loaded = False
        double_check = False
        k = 0

        if sleep_time:
            time.sleep(sleep_time)

        # Get source code of the page to track changes in HTML:
        source = ''
        try:
            source = self.driver.page_source
        except:
            pass

        # Wait until page loaded (and scroll it, to make sure all objects will be loaded):
        while not page_loaded:
            time.sleep(0.5)
            k += 1

            if check_js_complete:
                # Scroll down and wait when page will be loaded:
                try:
                    self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                    page_loaded = self.driver.execute_script("return document.readyState == 'complete';")
                except Exception as e:
                    pass

            if page_loaded and check_page_changes:
                # Check if the page source was changed
                new_source = ''
                try:
                    new_source = self.driver.page_source
                except:
                    pass

                page_loaded = new_source == source
                source = new_source

            # Wait when some element will disappear:
            if page_loaded and wait_for_xpath_to_disappear:
                bad_element = None

                try:
                    bad_element = WebDriverWait(self.driver, 0.1).until(
                        EC.presence_of_element_located((By.XPATH, wait_for_xpath_to_disappear))
                    )
                except:
                    pass  # Ignore timeout errors

                page_loaded = not bad_element

            if page_loaded and wait_for_element:
                try:
                    page_loaded = WebDriverWait(self.driver, 0.1).until(
                        EC.element_to_be_clickable(wait_for_element.locator)
                    )
                except:
                    pass  # Ignore timeout errors

            assert k < timeout, 'The page loaded more than {0} seconds!'.format(timeout)

            # Check two times that page completely loaded:
            if page_loaded and not double_check:
                page_loaded = False
                double_check = True

        # Go up:
        self.driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')

    # # Методы open page, wait_for_animation, wait_for_ajax_loading в рамках текущего проекта неактивны (не
    # используются)

    # def open_page(self, driver, url):
    #     """ This is advanced function which also checks that all images completely loaded. """
    #
    #     driver.get(url)
    #
    #     page_loaded = False
    #     images_loaded = False
    #
    #     script = ("return arguments[0].complete && typeof arguments[0].natural"
    #               "Width != \"undefined\" && arguments[0].naturalWidth > 0")
    #
    #     # Wait until page loaded (and scroll it, to make sure all objects will be loaded):
    #     while not page_loaded and not images_loaded:
    #         time.sleep(1)
    #
    #         # Scroll down and wait when page will be loaded:
    #         driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    #         page_loaded = driver.execute_script("return document.readyState == 'complete';")
    #
    #         # Make sure that every image loaded completely
    #         # (sometimes we have to scroll to the image to push browser upload it):
    #         pictures = driver.find_elements(By.XPATH, '//img')
    #         res = []
    #
    #         for image in pictures:
    #             src = image.get_attribute('src')
    #             if src:
    #                 # Scroll down to each image on the page:
    #                 image.location_once_scrolled_into_view
    #                 driver.execute_script("window.scrollTo(0, 155)")
    #
    #                 image_ready = driver.execute_script(script, image)
    #
    #                 if not image_ready:
    #                     # if the image not ready, give it a try to load and check again:
    #                     time.sleep(5)
    #                     image_ready = driver.execute_script(script, image)
    #
    #                 res.append(image_ready)
    #
    #         # Check that every image loaded and has some width > 0:
    #         images_loaded = False not in res
    #
    #     # Go up:
    #     driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')
    #
    # def wait_for_animation(self, driver, selector):
    #     """Waits until jQuery animations have finished for the given jQuery  selector."""
    #
    #     WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return jQuery(%s).is(":animated")'
    #                                                                          % json.dumps(selector)) == False)
    #
    # def wait_for_ajax_loading(self, driver, class_name):
    #     """Waits until the ajax loading indicator disappears."""
    #
    #     WebDriverWait(driver, 10).until(lambda driver: len(driver.find_elements(By.CLASS_NAME, class_name)) == 0)
