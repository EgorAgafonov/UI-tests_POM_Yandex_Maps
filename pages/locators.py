from selenium.webdriver.common.by import By


class MapPageLocators:
    MAP_SEARCH_FIELD = (By.XPATH, "//input[@placeholder='Поиск мест и адресов']")
    MAP_SUBMIT_SEARCH_BTN = (By.XPATH, "//button[@aria-label='Найти']")
    MAP_MY_GEOLOC_BTN = (By.XPATH, "//button[@aria-label='Моё местоположение']")
    MAP_INCRISE_VIEW_SIZE = (By.XPATH, "//button[@aria-label='Приблизить']")
    MAP_DECREASE_VIEW_SIZE = (By.XPATH, "//button[@aria-label='Отдалить']")
    MAP_TOPONYM_DESCRIPTION = (By.XPATH, "//ul/li[1]/div/div/div/div[2]/div[1]/div[1]")
    MAP_SWITCH_TO_3D_MAP_BTN = (By.CSS_SELECTOR, "div[class='map-tilt-rotate-control__tilt']")
    MAP_BUILD_ROUTE_BTN = (By.XPATH, "//a[@title='Построить маршрут']")
    MAP_DEPARTURES_ADDRESS_FIELD = (By.CSS_SELECTOR, "input[placeholder='Откуда']")
    MAP_DESTINATION_ADDRESS_FIELD = (By.CSS_SELECTOR, "input[placeholder='Куда']")
    MAP_EXPECTED_TIME_OF_ARRIVAL = (By.CSS_SELECTOR, "div[class='auto-route-snippet-view__arrival']")


