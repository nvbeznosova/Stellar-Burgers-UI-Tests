from selenium.webdriver.common.by import By

class ConstructorPageLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")  # Вкладка "Булки"
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")  # Вкладка "Соусы"
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")  # Вкладка "Начинки"
