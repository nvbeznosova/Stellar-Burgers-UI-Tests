from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_INPUT = (By.NAME, "email")  # Поле ввода Email
    PASSWORD_INPUT = (By.NAME, "password")  # Поле ввода Пароль
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной
    LOGIN_BUTTON_FORM = (By.XPATH, "//button[text()='Войти']")  # Кнопка входа в формах
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный кабинет']")  # Кнопка "Личный кабинет"
    RESTORE_PASSWORD_BUTTON = (By.LINK_TEXT, "Восстановить пароль")  # Кнопка восстановления пароля
