from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_SEARCH_FIELD = (By.CSS_SELECTOR, "#app > div.ad_branding_header > div > div > div.rc__781Li.rc__o-jux > div > form > input")
    MAIN_SUBMIT_SEARCH_BTN = (By.CSS_SELECTOR, "#app > div.ad_branding_header > div > div > div.rc__781Li.rc__o-jux > div > form > button")
    MAIN_NEWS_BTN = (By.CSS_SELECTOR, "#app > div.ad_branding_header > header > div > div > nav > div:nth-child(1) > a")


# class AuthLocators:
#     AUTH_EMAIL = (By.ID, "email")
#     AUTH_PASS = (By.ID, "pass")
#     AUTH_BTN = (By.CLASS_NAME, "btn-success")
#     AUTH_ALERT_MSG = (By.XPATH, "//div[@role='alert']")
