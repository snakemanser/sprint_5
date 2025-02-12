from selenium.webdriver.common.by import By

class Locators:
    BUTTON_ENTER_INTO_ACC = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")  # Кнопка "Войти в аккаунт"
    LINK_REGISTER = (By.XPATH, "//a[@href = '/register']") # Ссылка "Зарегистрироваться"
    REGISTER_NAME = (By.XPATH, "//label[contains(text(), 'Имя')]/parent::*/input")  # Поле регистрации имя
    REGISTER_EMAIL = (By.XPATH, "//label[contains(text(), 'Email')]/parent::*/input")  # Поле регистрации email
    REGISTER_PASS = (By.XPATH, "//label[contains(text(), 'Пароль')]/parent::*/input")  # Поле регистрации пароль
    BUTTON_REGISTER = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")  # Кнопка "Зарегистрироваться"
    BUTTON_LOGIN = (By.XPATH, "//button[contains(text(), 'Войти')]")  # Кнопка "Войти"
    LOGIN_EMAIL = (By.XPATH, "//label[contains(text(), 'Email')]/parent::*/input")  # Поле авторизации email
    LOGIN_PASS = (By.XPATH,"//label[contains(text(), 'Пароль')]/parent::*/input")  # Поле авторизации пароль
    BUTTON_ORDER = (By.XPATH, "//button[@class ='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")  # Кнопка "Оформить заказ"
    MESS_INCORRECT_PASS_REGISTER = (By.XPATH, "//p[@class='input__error text_type_main-default']")  # Сообщение об ошибке "Некорректный пароль" в форме регистрации
    MESS_ENTRANCE_LOGIN = (By.XPATH, "//h2[contains(text(),'Вход')]")  # Текст "Вход" на странице авторизации
    PERSONAL_ACC = (By.XPATH, "//a[@href='/account']")  # Личный кабинет
    LINK_AUTH = (By.XPATH, "//a[@href='/login']")  # Ссылка "Войти" в форме регистрации
    LINK_FORGOT_PASS = (By.XPATH, "//a[@href='/forgot-password']")  # Ссылка "Восстановить пароль" в форме авторизации
    MESS_PERSONAL_ACC_INFO = (By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default']")  # Текст "В этом разделе вы можете изменить свои персональные данные" в личном кабинете
    CONSTRUCTOR = (By.XPATH, "//p[contains(text(), 'Конструктор')]")  # Конструктор
    LOGO_STELLAR_BURGERS = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a/*")  # Логотип Stellar Burgers
    BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(),'Выход')]")  # Кнопка "Выход" в личном кабинете
    BUNS = (By.XPATH, "//span[contains(text(),'Булки')]")  # Раздел "Булки"
    SAUCES = (By.XPATH, "//span[contains(text(),'Соусы')]")  # Раздел "Соусы"
    FILLINGS = (By.XPATH, "//span[contains(text(),'Начинки')]")  # Раздел "Начинки"
    CHEESE = (By.XPATH, "//p[contains(text(),'Сыр с астероидной плесенью')]")  # Сыр с астероидной плесенью, начинка
    MESS_BUNS = (By.XPATH, "//h2[contains(text(),'Булки')]")  # Текст "Булки" в конструкторе
    CONTAINER = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']")  # Контейнер со скролом в конструкторе




