from selenium.webdriver.common.by import By


class AuthLocators:
    AUTH_EMAIL = (By.ID, "email")
    AUTH_PASS = (By.ID, "pass")
    AUTH_BTN = (By.CLASS_NAME, "btn-success")
    AUTH_ALERT_MSG = (By.XPATH, "//div[@role='alert']")


class MyPetsLocators:
    MY_PETS_NEW_PET_BTN = (By.CSS_SELECTOR, "html > body > div > div > div:nth-of-type(2) > div > button")
    MY_PETS_SUBMIT_PET_BTN = (By.XPATH, "//button[@onclick='add_pet();']")
    MY_PETS_DELETE_PET_BTN = (By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr:nth-child(1) > td.smart_cell > a > "
                                               "div")
    MY_PETS_CARDS_QUANTITY = (By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr")
    MY_PETS_PHOTO = (By.ID, "photo")
    MY_PETS_NAME = (By.ID, "name")
    MY_PETS_BREED = (By.ID, "animal_type")
    MY_PETS_AGE = (By.ID, "age")

