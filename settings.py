from dotenv import load_dotenv
import os
from random import randint

load_dotenv()
email = os.getenv('email')
password = os.getenv('pass')
invalid_email = os.getenv('invalid_email')
invalid_password = os.getenv('invalid_pass')


def strings_generator(n):
    return "x" * n


def russian_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def chinese_chars():
    return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


def digits():
    return '1234567890'


def latin_chars():
    return 'abcdefghijklmnopqrstwxyz'


def random_num(start=1, end=10000):
    num = randint(start, end)
    return str(num)


screenshots_folder = os.path.abspath("C:\\Users\\agafo\\PycharmProjects\\YandexMaps\\screens")
