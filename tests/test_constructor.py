import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from locators.constructor_page_locators import ConstructorPageLocators

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_constructor_tabs(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*ConstructorPageLocators.BUNS_TAB).click()
    driver.find_element(*ConstructorPageLocators.SAUCES_TAB).click()
    driver.find_element(*ConstructorPageLocators.FILLINGS_TAB).click()