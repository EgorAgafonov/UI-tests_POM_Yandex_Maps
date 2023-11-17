from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_SEARCH_FIELD = (By.ID, "1")
    MAIN_SUBMIT_SEARCH_BTN = (By.XPATH, "//button[@class='c-text-field__search-button']")
    MAIN_CATALOG_BTN = (By.XPATH, "//div[@class='header-main__catalog-btn']")


# class AuthLocators:
#     AUTH_EMAIL = (By.ID, "email")
#     AUTH_PASS = (By.ID, "pass")
#     AUTH_BTN = (By.CLASS_NAME, "btn-success")
#     AUTH_ALERT_MSG = (By.XPATH, "//div[@role='alert']")
