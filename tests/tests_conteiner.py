from constants import ConstantsScript
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class TestStellarBurgersContainer:

    # Переходы к разделам булки, соусы, начинки

    # К булкам
    def test_moving_to_buns(self, driver, login):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER))
        # Получаем текущую позицию прокрутки внутри контейнера
        initial_scroll_position = driver.execute_script(ConstantsScript.scrollTopScript, driver.find_element(*Locators.CONTAINER))
        # Скролим до сыра
        element = driver.find_element(*Locators.CHEESE)
        driver.execute_script(ConstantsScript.scrollIntoViewScript, element)
        # Кликаем по разделу "Булки"
        driver.find_element(*Locators.BUNS).click()
        # Получаем текущую позицию прокрутки внутри контейнера
        final_scroll_position = driver.execute_script(ConstantsScript.scrollTopScript, driver.find_element(*Locators.CONTAINER))
        # Для проверОчки результаты позиций печатаем
        print(f"Initial scroll position: {initial_scroll_position}")
        print(f"Final scroll position: {final_scroll_position}")
        # Проверяем, что прокрутка произошла
        assert final_scroll_position > initial_scroll_position

    # К соусам
    def test_moving_to_sauces(self, driver, login):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER))
        # Получаем текущую позицию прокрутки внутри контейнера
        initial_scroll_position = driver.execute_script(ConstantsScript.scrollTopScript, driver.find_element(*Locators.CONTAINER))
        # Скролим до сыра
        element = driver.find_element(*Locators.CHEESE)
        driver.execute_script(ConstantsScript.scrollIntoViewScript, element)
        # Кликаем по разделу "Соусы"
        driver.find_element(*Locators.SAUCES).click()
        # Получаем текущую позицию прокрутки внутри контейнера
        final_scroll_position = driver.execute_script(ConstantsScript.scrollTopScript, driver.find_element(*Locators.CONTAINER))
        # Для проверОчки результаты позиций печатаем
        print(f"Initial scroll position: {initial_scroll_position}")
        print(f"Final scroll position: {final_scroll_position}")
        # Проверяем, что прокрутка произошла
        assert final_scroll_position > initial_scroll_position

    # К начинкам
    def test_moving_to_fillings(self, driver, login):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER))
        # Получаем текущую позицию прокрутки внутри контейнера
        initial_scroll_position = driver.execute_script(ConstantsScript.scrollTopScript, driver.find_element(*Locators.CONTAINER))
        # Кликаем по разделу "Начинки"
        driver.find_element(*Locators.FILLINGS).click()
        # Получаем текущую позицию прокрутки внутри контейнера
        final_scroll_position = driver.execute_script(ConstantsScript.scrollTopScript, driver.find_element(*Locators.CONTAINER))
        # Для проверОчки результаты позиций печатаем
        print(f"Initial scroll position: {initial_scroll_position}")
        print(f"Final scroll position: {final_scroll_position}")
        # Проверяем, что прокрутка произошла
        assert final_scroll_position > initial_scroll_position
