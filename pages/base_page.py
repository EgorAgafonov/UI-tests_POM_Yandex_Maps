from urllib.parse import urlparse
from settings import screenshots_folder
from colorama import Style, Fore
import time
from termcolor import colored

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    """Базовый(родительский) класс веб-страницы. Определяет основные методы взаимодействия со страницами в рамках
    проектирования UI-тестов по паттерну PageObjectModel. Создан для наследования последующими классами веб-страниц,
    в свою очередь, содержащих методы управления элементами каждой конкретной страницы сайта https://www.mvideo.ru/."""

    driver = None

    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def refresh_page(self):
        self.driver.refresh()

    def make_screenshot(self, file_path=screenshots_folder):
        self.driver.save_screenshot(file_path)

    def scroll_down(self, offset=0):
        """Метод прокрутки страницы вниз."""

        if offset:
            self.driver.execute_script(f'window.scrollTo(0, {offset});')
        else:
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def scroll_up(self, offset=0):
        """Метод прокрутки страницы вниз."""

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

    def wait_page_loaded(self, timeout=60, check_js_complete=True,
                         check_page_changes=False, check_images=False,
                         wait_for_element=None,
                         wait_for_xpath_to_disappear='',
                         sleep_time=2):
        """ This function waits until the page will be completely loaded.
            We use many different ways to detect is page loaded or not:

            1) Check JS status
            2) Check modification in source code of the page
            3) Check that all images uploaded completely
               (Note: this check is disabled by default)
            4) Check that expected elements presented on the page
        """

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
                        EC.element_to_be_clickable(wait_for_element._locator)
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
