from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    # chrome_driver.implicitly_wait(7)  # Не явное ожидание
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)


def test_clear(driver):
    input_data = "sdgfdsgddsfdfs"
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.NAME, 'text_string')
    text_string.send_keys(input_data)
    sleep(2)
    # text_string.clear()
    entered_value = text_string.get_attribute('value')
    for _ in range(len(entered_value)):
        text_string.send_keys(Keys.BACKSPACE)
    assert text_string.is_displayed()


def test_enabled_and_select(driver):
    driver.get('https://www.qa-practice.com/elements/button/disabled')
    button = driver.find_element(By.NAME, 'submit')
    print(button.is_enabled())
    select = driver.find_element(By.ID, 'id_select_state')
    dropdown = Select(select)
    dropdown.select_by_value('enabled')
    print(button.is_enabled())


def test_welcome(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    button_3 = driver.find_element(By.ID, 'visibleAfter')
    button_3.click()


def test_cart(driver):
    driver.get('https://magento.softwaretestingboard.com/olivia-1-4-zip-light-jacket.html')
    size = driver.find_element(By.ID, 'option-label-size-143-item-166')
    color = driver.find_element(By.ID, 'option-label-color-93-item-50')
    button = driver.find_element(By.ID, 'product-addtocart-button')
    size.click()
    color.click()
    button.click()
    wait = WebDriverWait(driver, 5)
    wait.until_not(
        EC.text_to_be_present_in_element_attribute(
            (By.CSS_SELECTOR, '.counter.qty'),
            'class',
            'empty'
        )
    )
    counter = driver.find_element(By.CSS_SELECTOR, '.counter-number')
    print(counter.text)


# TODO не рабочий тест, зависате на странице!!!
def test_5_sec2(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'visibleAfter')))
    button_3 = driver.find_element(By.ID, 'visibleAfter')
    button_3.click()


""""Добавление кук"""


def test_cookie(driver):
    driver.get('https://www.qa-practice.com/elements/button/disabled')
    driver.add_cookie({'name': 'testname', 'value': 'test'})
    print()
    print(driver.get_cookies())


"""Поиск одинаковых элементов и обращение к ним как к списку"""


def test_same_elements(driver):
    driver.get('https://magento.softwaretestingboard.com/men/bottoms-men/pants-men.html')
    sleep(2)
    product_link = driver.find_elements(By.CLASS_NAME, 'product-item-link')
    print(product_link[-1].text)


def test_same_cards(driver):
    driver.get('https://magento.softwaretestingboard.com/men/bottoms-men/pants-men.html')
    sleep(2)
    product_cart = driver.find_elements(By.CLASS_NAME, 'product-item-info')
    for cart in product_cart:
        print(cart.find_element(By.CLASS_NAME,'price').text)

    #print(product_link[0].find_element(By.CLASS_NAME,'price').text)
