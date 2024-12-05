from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class TestStellarBurgersRedirects:

    # тесты переходов на страницу авторизации

    # переход по кнопке «Войти в аккаунт» на главной
    def test_button_enter_into_acc_redirect_to_login_page(self, driver):
        driver.find_element(*Locators.BUTTON_ENTER_INTO_ACC).click()
        element = driver.find_element(*Locators.MESS_ENTRANCE_LOGIN).text
        assert element


    # переход через кнопку «Личный кабинет»
    def test_personal_acc_redirect_to_login_page(self, driver):
        driver.find_element(*Locators.PERSONAL_ACC).click()
        element = driver.find_element(*Locators.MESS_ENTRANCE_LOGIN).text
        assert element


    # переход через кнопку в форме регистрации
    def test_auth_link_redirect_to_login_page(self, driver):
        driver.find_element(*Locators.BUTTON_ENTER_INTO_ACC).click()
        driver.find_element(*Locators.LINK_REGISTER).click()
        driver.find_element(*Locators.LINK_AUTH).click()
        element = driver.find_element(*Locators.MESS_ENTRANCE_LOGIN).text
        assert element


    # переход через кнопку в форме восстановления пароля
    def test_auth_link_forgot_pass_page_redirect_to_login_page(self, driver):
        driver.find_element(*Locators.BUTTON_ENTER_INTO_ACC).click()
        driver.find_element(*Locators.LINK_FORGOT_PASS).click()
        driver.find_element(*Locators.LINK_AUTH).click()
        element = driver.find_element(*Locators.MESS_ENTRANCE_LOGIN).text
        assert element


    # Переход в личный кабинет

    def test_entrance_to_personal_acc(self, driver, login):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER))
        driver.find_element(*Locators.PERSONAL_ACC).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.MESS_PERSONAL_ACC_INFO))
        element = driver.find_element(*Locators.MESS_PERSONAL_ACC_INFO).text
        assert element


    # Переход из личного кабинета в конструктор

    # переход по клику на «Конструктор»
    def test_entrance_to_constructor_click_constructor(self, driver, login):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER))
        driver.find_element(*Locators.PERSONAL_ACC).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.MESS_PERSONAL_ACC_INFO))
        driver.find_element(*Locators.CONSTRUCTOR).click()
        element = driver.find_element(*Locators.BUTTON_ORDER).text
        assert element


    # переход по клику на логотип Stellar Burgers
    def test_entrance_to_constructor_click_logo(self, driver, login):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER))
        driver.find_element(*Locators.PERSONAL_ACC).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.MESS_PERSONAL_ACC_INFO))
        driver.find_element(*Locators.LOGO_STELLAR_BURGERS).click()
        element = driver.find_element(*Locators.BUTTON_ORDER).text
        assert element


    # Выход из аккаунта

    def test_logout(self, driver, login):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER))
        driver.find_element(*Locators.PERSONAL_ACC).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.MESS_PERSONAL_ACC_INFO))
        driver.find_element(*Locators.BUTTON_LOGOUT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.MESS_ENTRANCE_LOGIN))
        element = driver.find_element(*Locators.MESS_ENTRANCE_LOGIN).text
        assert element
