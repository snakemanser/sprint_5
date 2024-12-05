import pytest
from selenium import webdriver
from locators import Locators

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.nomoreparties.site/')
    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.BUTTON_ENTER_INTO_ACC).click()
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys('vitaliy.shmulyaev.16322@qa.qa')
    driver.find_element(*Locators.LOGIN_PASS).send_keys('123456')
    driver.find_element(*Locators.BUTTON_LOGIN).click()
    return driver
