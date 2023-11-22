from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_SEARCH_FIELD = (By.XPATH, "//input[@placeholder='Поиск мест и адресов']")
    MAIN_SUBMIT_SEARCH_BTN = (By.XPATH, "//button[@aria-label='Найти']")
    MAIN_MY_GEO_BTN = (By.XPATH, "//button[@aria-label='Моё местоположение']")
    MAIN_INCRISE_VIEW_SIZE = (By.XPATH, "//button[@aria-label='Приблизить']")
    MAIN_DICRISE_VIEW_SIZE = (By.XPATH, "//button[@aria-label='Отдалить']")
    MAIN_TOPONYM_DESCRIPTION = (By.XPATH, "//ul/li[1]/div/div/div/div[2]/div[1]/div[1]")
    MAIN_3D_TILT_ROTATE_BTN = (By.XPATH, "//div[@style='transform: rotateX(0rad);']")


# class AuthLocators:
#     AUTH_EMAIL = (By.ID, "email")
#     AUTH_PASS = (By.ID, "pass")
#     AUTH_BTN = (By.CLASS_NAME, "btn-success")
#     AUTH_ALERT_MSG = (By.XPATH, "//div[@role='alert']")
