import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from locators.personal_account_locators import PersonalAccountLocators

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_redirect_to_personal_account(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*PersonalAccountLocators.EMAIL_INPUT).send_keys("существующий_email")
    driver.find_element(*PersonalAccountLocators.PASSWORD_INPUT).send_keys("существующий_пароль")
    driver.find_element(*PersonalAccountLocators.LOGIN_BUTTON).click()
    driver.find_element(*PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON).click()
    assert "account" in driver.current_url

def test_logout_from_personal_account(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*PersonalAccountLocators.EMAIL_INPUT).send_keys("существующий_email")
    driver.find_element(*PersonalAccountLocators.PASSWORD_INPUT).send_keys("существующий_пароль")
    driver.find_element(*PersonalAccountLocators.LOGIN_BUTTON).click()
    driver.find_element(*PersonalAccountLocators.LOGOUT_BUTTON).click()
    assert "login" in driver.current_url
    