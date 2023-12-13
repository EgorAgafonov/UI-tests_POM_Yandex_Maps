Коллекция UI-тестов на базе фреймворков Pytest и Selenium для функционального
тестирования веб-приложения "Яндекс.Карты".


При проектировании модуля и тестовых функций использовался паттерн PageObject. 
Основная структура проекта представлена:
1) папкой pages с родительским классом BasePage и наследованным от него классом MainPage, содержащими основные атрибуты
и методы для взаимодействия с тестируемой веб-платформой и её элементами;
2) папкой tests с коллекцией позитивных UI-тестов для платформы "Яндекс.Карты".
3) папками logs и screens, хранящими артефакты результатов тестирования. 

В корневой папке проекта содержатся модули settings.py и conftest.py с необходимыми тестовыми данными и 
фикстурами(декораторами) Pytest для инициализации setup-настроек запуска тестовых функций.

Используются версии фреймворков Selenium ver.4.15.2 и PyTest ver.7.4.3.

Каждый тест и класс в модулях содержат подробную аннотацию к выполняемому коду. 

ВАЖНО: Код всех авто-тестов в настоящем проекте использует драйвер браузера Google Chrome. Коллекция спроектирована с
использованием версии Selenium 4.15.2, тесты не требуют обязательной установки драйвера Chrome и плагина
pytest-selenium. Тесты запускаются как из текстового редактора IDLE PyCharm, так и с помощью команды в терминале.

Для запуска тестов (в Python ver.3 и выше) из терминала достаточно перейти в директорию папки tests и выполнить команду:

pytest map_page_positive.py

Для удобства запуска определенного теста и/или группы тестов из терминала, каждая тестовая функция содержит 
фикстуру pytest.mark.<пользовательское имя функции>.

Пример запуска функции test_search_address_positive из терминала:

pytest map_page_positive.py -v -m"search_address"

Агафонов Е.А., 2023 г.
