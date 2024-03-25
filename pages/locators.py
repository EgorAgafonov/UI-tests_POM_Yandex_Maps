from selenium.webdriver.common.by import By


class MapPageLocators:
    """Класс переменных для определения локаторов элементов на странице "https://yandex.ru/maps"""

    MAP_SEARCH_FIELD = (By.CSS_SELECTOR, "input[placeholder='Поиск мест и адресов']")
    MAP_MY_GEOLOC_BTN = (By.CSS_SELECTOR, "button[aria-label='Моё местоположение']")
    MAP_MY_GEOLOC_NAME = (By.CSS_SELECTOR, "h1[class='home-panel-content-view__header-text']")
    MAP_CLEAR_FIELD_BTN = (By.CSS_SELECTOR, "button[aria-label='Закрыть']")
    MAP_INCREASE_VIEW_SIZE = (By.CSS_SELECTOR, "button[aria-label='Приблизить']")
    MAP_DECREASE_VIEW_SIZE = (By.CSS_SELECTOR, "button[aria-label='Отдалить']")
    MAP_SCALE_LINE = (By.CSS_SELECTOR, "div[class='map-scale-line__label']")
    #
    MAP_CHOOSE_MODE_VIEW = (By.CSS_SELECTOR, "button[aria-label='Слои']")
    MAP_CHOOSE_SCHEME_VIEW = (By.CSS_SELECTOR, "div[aria-label='Схема']")
    MAP_CHOOSE_SPUTNIK_VIEW = (By.CSS_SELECTOR, "div[aria-label='Спутник']")
    MAP_CHOOSE_HYBRID_VIEW = (By.CSS_SELECTOR, "div[aria-label='Гибрид']")
    MAP_STREET_PANORAMA_VIEW = (By.CSS_SELECTOR, "a[aria-label='Панорамы улиц и фотографии']")
    MAP_CLOSE_PANORAMA_VIEW = (By.CSS_SELECTOR, "div[class='panorama-controls-view__close']")
    #
    MAP_TOPONYM_DESCRIPTION = (By.LINK_TEXT, "Музей космонавтики")
    MAP_SWITCH_TO_3D_MAP_BTN = (By.CSS_SELECTOR, "div[class='map-tilt-rotate-control__tilt']")
    MAP_SWITCH_OFF_3D_MAP_BTN = (By.CSS_SELECTOR, "div[class='map-tilt-rotate-control__tilt-wrapper']")
    MAP_BUILD_ROUTE_BTN = (By.CSS_SELECTOR, "a[aria-label='Построить маршрут']")
    #
    MAP_ROUTE_BY_CAR_BTN = (By.CSS_SELECTOR, "div[aria-label='На автомобиле']")
    MAP_ROUTE_BY_CITY_TRANSPORT_BTN = (By.CSS_SELECTOR, "div[aria-label='На общественном транспорте']")
    MAP_ROUTE_BY_WALKING_BTN = (By.CSS_SELECTOR, "div[aria-label='Пешком']")
    #
    MAP_DEPARTURES_ADDRESS_FIELD = (By.CSS_SELECTOR, "input[placeholder='Откуда']")
    MAP_DESTINATION_ADDRESS_FIELD = (By.CSS_SELECTOR, "input[placeholder='Куда']")
    MAP_EXPECTED_TIME_OF_ARRIVAL_CAR = (By.CSS_SELECTOR, "div[class='auto-route-snippet-view__arrival']")
    MAP_EXPECTED_TIME_OF_ARRIVAL_CITY_TRNSPRT = (By.CSS_SELECTOR, "div[class='masstransit-route-snippet-view__route"
                                                                  "-hint']")
    MAP_TRAVEL_TIME_BY_FOOT = (By.CSS_SELECTOR, "div[class='pedestrian-route-snippet-view__route-title-primary']")
    MAP_TRAFFIC_BTN = (By.CSS_SELECTOR, "a[aria-label='Пробки в Москве']")
    MAP_CITY_TRANSPORT = (By.CSS_SELECTOR, "a[aria-label='Движущийся транспорт']")

    MAP_DETAILS_MENU = (By.CSS_SELECTOR, "button[aria-label='Детали']")
    MAP_METRO_SCHEME = (By.LINK_TEXT, "Схема метро")
    MAP_DEPARTURE_METRO_STATION_FIELD = (By.CSS_SELECTOR, "input[placeholder='Откуда']")
    MAP_DESTINATION_METRO_STATION_FIELD = (By.CSS_SELECTOR, "input[placeholder='Куда']")
    MAP_METRO_RIDES_DURATION = (By.CSS_SELECTOR, "div[class='masstransit-route-snippet-view__route-duration']")
