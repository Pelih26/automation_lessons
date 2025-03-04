from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    # chrome_driver.implicitly_wait(6)  # Не явное ожидание
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)


# TODO Переход на другую вкладку
def test_new_tab(driver):
    driver.get('https://www.qa-practice.com/elements/new_tab/link')
    driver.find_element(By.ID, 'new-page-link').click()
    # print(driver.window_handles)
    tabs = driver.window_handles      # ID Вкладки
    driver.switch_to.window(tabs[1])  # Выбор на какую вкладку переключиться
    result = driver.find_element(By.ID, 'result-text')
    assert result.text == 'I am a new page in a new tab'
    driver.close()   # Закрыть вкладку на которую переключились
    driver.switch_to.window(tabs[0])   # Переключиться обратно на первую вкладку


def test_iframe(driver):
    driver.get('https://www.qa-practice.com/elements/iframe/iframe_page')
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    driver.find_element(By.CLASS_NAME, 'navbar-toggler').click()
    driver.switch_to.default_content()
    driver.find_element(By.LINK_TEXT, 'Iframe').click()


# TODO Вызов ошибки 'no such element'
def test_stale_exception(driver):
    driver.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')
    checkbox = driver.find_element(By.ID, 'checkbox')
    checkbox.click()
    print(checkbox.id)
    submit = driver.find_element(By.ID, 'submit-id-submit')
    submit.click()
    print(submit.id)
    assert driver.find_element(By.ID, 'result-text').text == 'select me or not'
    # TODO Вызовет ошибку 'no such element' так как элемента в памяти selenium уже не существует
    checkbox.click()
    submit.click()


def test_drop_menu(driver):
    driver.implicitly_wait(5)
    driver.get('https://magento.softwaretestingboard.com/')
    women = driver.find_element(By.ID, 'ui-id-4')
    tops = driver.find_element(By.ID, 'ui-id-9')
    jackets = driver.find_element(By.ID, 'ui-id-11')
    # ActionChains(driver).move_to_element(women).move_to_element(tops).move_to_element(jackets).click(jackets).perform()
    actions = ActionChains(driver)
    actions.move_to_element(women)
    actions.move_to_element(tops)
    actions.move_to_element(jackets)
    actions.click(jackets)
    actions.perform()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Jackets'
    # actions.context_click(women)   # TODO Вызвать контекстное меню правой клавишей мышы


def test_d_n_d(driver):
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    first = driver.find_element(By.ID, 'rect-draggable')
    second = driver.find_element(By.ID, 'rect-droppable')
    ActionChains(driver).drag_and_drop(first, second).perform()
    """ МОЖНО ВОТ ТАК 
    actions = ActionChains(driver)
    actions.click_and_hold(first)
    actions.move_to_element(second)
    actions.release()
    actions.perform()
    """



# TODO Сочетание нажатия клавищи на клавиатуре + клавиша на мышке
def test_open_in_new_tab(driver):
    driver.get('https://www.qa-practice.com/')
    link = driver.find_element(By.LINK_TEXT, 'Homepage')
    ActionChains(driver).key_down(Keys.COMMAND).click(link).key_up(Keys.COMMAND).perform()


# TODO Сочетание нажатия клавищи на клавиатуре + клавиша на мышке
def test_alerts(driver):
    driver.get('https://www.qa-practice.com/elements/alert/alert#')
    driver.find_element(By.CLASS_NAME, 'a-button').click()
    alert_box = Alert(driver)
    alert_box.accept()