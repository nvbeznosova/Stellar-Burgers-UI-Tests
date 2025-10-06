from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле "Имя"
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле "Email"
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле "Пароль"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class,'input__error')]")  # Сообщение об ошибке
    LOGIN_LINK = (By.LINK_TEXT, "Войти")  # Ссылка "Войти" из формы регистрации
