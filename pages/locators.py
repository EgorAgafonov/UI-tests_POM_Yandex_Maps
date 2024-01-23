from selenium.webdriver.common.by import By


class MapPageLocators:
    """Класс с методами определения локаторов элементов на странице "https://yandex.ru/maps"""

    MAP_SEARCH_FIELD = (By.XPATH, "//input[@placeholder='Поиск мест и адресов']")
    MAP_MY_GEOLOC_BTN = (By.XPATH, "//button[@aria-label='Моё местоположение']")
    MAP_CLEAR_FIELD_BTN = (By.CSS_SELECTOR, "button[aria-label='Закрыть']")
    MAP_INCRISE_VIEW_SIZE = (By.XPATH, "//button[@aria-label='Приблизить']")
    MAP_DECREASE_VIEW_SIZE = (By.XPATH, "//button[@aria-label='Отдалить']")
    MAP_TOPONYM_DESCRIPTION = (By.LINK_TEXT, "Музей космонавтики")
    MAP_SWITCH_TO_3D_MAP_BTN = (By.CSS_SELECTOR, "div[class='map-tilt-rotate-control__tilt']")
    MAP_BUILD_ROUTE_BTN = (By.CSS_SELECTOR, "a[aria-label='Построить маршрут']")
    MAP_DEPARTURES_ADDRESS_FIELD = (By.CSS_SELECTOR, "input[placeholder='Откуда']")
    MAP_DESTINATION_ADDRESS_FIELD = (By.CSS_SELECTOR, "input[placeholder='Куда']")
    MAP_EXPECTED_TIME_OF_ARRIVAL = (By.CSS_SELECTOR, "div[class='auto-route-snippet-view__arrival']")
    MAP_TRAFFIC_BTN = (By.CSS_SELECTOR, "a[aria-label='Пробки в Москве']")
    MAP_CITY_TRANSPORT = (By.CSS_SELECTOR, "a[aria-label='Движущийся транспорт']")

