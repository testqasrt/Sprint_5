from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import RegisteredUser
from locators import (constructor_button, constructor_title, login_form_header,
                      personal_cabinet_button, personal_page_logout_button,
                      personal_page_profile_button)
from urls import BASE_URL, LOGIN_PAGE_URL, USER_PAGE


class TestPersonal:
    def test_go_to_personal_page(self, driver, auth):
        user = RegisteredUser()
        auth(driver, user.email, user.password)
        driver.find_element(*personal_cabinet_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            personal_page_profile_button))
        assert driver.find_element(*personal_page_profile_button).is_displayed()
        assert driver.current_url == USER_PAGE

    def test_go_to_constructor_from_personal_page(self, driver, auth):
        user = RegisteredUser()
        auth(driver, user.email, user.password)
        driver.find_element(*constructor_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(constructor_button))
        driver.find_element(*constructor_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(constructor_title))
        assert driver.find_element(*constructor_title).is_displayed()
        assert driver.current_url == BASE_URL

    def test_logout_from_personal_page(self, driver, auth):
        user = RegisteredUser()
        auth(driver, user.email, user.password)
        driver.find_element(*personal_cabinet_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            personal_page_logout_button))
        driver.find_element(*personal_page_logout_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(login_form_header))
        assert driver.current_url == LOGIN_PAGE_URL
