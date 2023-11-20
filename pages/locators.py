from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_SEARCH_FIELD = (By.XPATH, "//input[@placeholder='Поиск мест и адресов']")
    MAIN_SUBMIT_SEARCH_BTN = (By.XPATH, "//button[@aria-label='Найти']")
    # MAIN_CATALOG_BTN = (By.CSS_SELECTOR, "#stickyHeader > div.dn6 > div > div > button")


# class AuthLocators:
#     AUTH_EMAIL = (By.ID, "email")
#     AUTH_PASS = (By.ID, "pass")
#     AUTH_BTN = (By.CLASS_NAME, "btn-success")
#     AUTH_ALERT_MSG = (By.XPATH, "//div[@role='alert']")
