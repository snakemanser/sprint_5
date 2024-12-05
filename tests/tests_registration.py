from faker import Faker

from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

faker = Faker()

class TestStellarBurgersRegistration:

    # тесты на регистрацию

    # регистрируем нового юзера и авторизуемся
    def test_registration(self, driver):
        name = 'Пудж'
        email = faker.email()
        password = '123456'
        driver.find_element(*Locators.BUTTON_ENTER_INTO_ACC).click()
        driver.find_element(*Locators.LINK_REGISTER).click()
        driver.find_element(*Locators.REGISTER_NAME).send_keys(name)
        driver.find_element(*Locators.REGISTER_EMAIL).send_keys(email)
        driver.find_element(*Locators.REGISTER_PASS).send_keys(password)
        driver.find_element(*Locators.BUTTON_REGISTER).click()
        # ждем пока появится кнопка "Войти", чтобы заполнить поля и кликнуть по войти
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_LOGIN))
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(email)
        driver.find_element(*Locators.LOGIN_PASS).send_keys(password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        # ждем пока выполнится логин, по зарегистрированным данным, чтобы проверить, что успешно вошли, потому что отображается кнопка "Оформить заказ"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER))
        element = driver.find_element(*Locators.BUTTON_ORDER).text
        assert element

    # получаем ошибку "Некорректный пароль" в форме регистрации
    def test_registration_123_password(self, driver):
        name = 'Падж'
        email = faker.email()
        password = '123'
        driver.find_element(*Locators.BUTTON_ENTER_INTO_ACC).click()
        driver.find_element(*Locators.LINK_REGISTER).click()
        driver.find_element(*Locators.REGISTER_NAME).send_keys(name)
        driver.find_element(*Locators.REGISTER_EMAIL).send_keys(email)
        driver.find_element(*Locators.REGISTER_PASS).send_keys(password)
        driver.find_element(*Locators.BUTTON_REGISTER).click()
        element = driver.find_element(*Locators.MESS_INCORRECT_PASS_REGISTER).text
        assert element == 'Некорректный пароль'
