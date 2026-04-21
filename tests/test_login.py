import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from locators.login_page_locators import LoginPageLocators

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_main_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON_MAIN).click()
