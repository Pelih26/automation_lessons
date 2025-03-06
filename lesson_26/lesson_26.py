from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    # chrome_driver.implicitly_wait(6)  # Не явное ожидание
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)


def test_scroll(driver):
    driver.get('https://www.onliner.by')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')  # Скролл до футера
    driver.execute_script('window.scrollTo(0, 500)')  # Скролл на кол-во пиксилей


def test_scroll_to_element(driver):
    driver.get('https://the-internet.herokuapp.com/')
    sleep(3)
    link = driver.find_element(By.LINK_TEXT, 'Secure File Download')
    driver.execute_script('arguments[0].scrollIntoView();', link)  # Скрол до определенной ссылке


# TODO Загрузка файла
def test_image(driver):
    driver.get('https://the-internet.herokuapp.com/upload')
    upload = driver.find_element(By.ID, 'file-upload')
    button = driver.find_element(By.ID, 'file-submit')
    upload.send_keys('/Users/k.pelikhovich/Downloads/test.jpg')
    sleep(3)
    button.click()
