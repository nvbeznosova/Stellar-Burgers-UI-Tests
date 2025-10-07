import pytest
from locators.constructor_page_locators import ConstructorPageLocators
from urls import BASE_URL

class TestConstructorTabs:

    def test_constructor_tabs(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*ConstructorPageLocators.SAUCES_TAB).click()
        assert driver.find_element(*ConstructorPageLocators.SAUCES_TAB_ACTIVE).is_displayed()

        driver.find_element(*ConstructorPageLocators.FILLINGS_TAB).click()
        assert driver.find_element(*ConstructorPageLocators.FILLINGS_TAB_ACTIVE).is_displayed()

        driver.find_element(*ConstructorPageLocators.BUNS_TAB).click()
        assert driver.find_element(*ConstructorPageLocators.BUNS_TAB_ACTIVE).is_displayed()
