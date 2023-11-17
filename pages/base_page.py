from urllib.parse import urlparse
from settings import screenshots_folder
from colorama import Style, Fore


class BasePage(object):
    """Базовый(родительский) класс веб-страницы. Определяет основные методы взаимодействия со страницами в рамках
    проектирования UI-тестов по паттерну PageObjectModel. Создан для наследования последующими классами веб-страниц,
    в свою очередь, содержащих методы управления элементами каждой конкретной страницы сайта https://www.mvideo.ru/."""

    driver = None

    def __init__(self, driver, url, timeout=15):
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
