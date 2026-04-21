from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    EMAIL_INPUT = (By.NAME, "email")  # Поле Email для входа
    PASSWORD_INPUT = (By.NAME, "password")  # Поле Пароль для входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка входа
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный кабинет']")  # Переход в личный кабинет
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")  # Кнопка "Выйти"
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")  # Переход в конструктор
    LOGO_LINK = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # Переход по клику на логотип
