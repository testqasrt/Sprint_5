import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import NewUser
from locators import login_form_header, wrong_password_error
from urls import LOGIN_PAGE_URL, REGISTRATION_PAGE_URL


class TestRegistration:
    def test_successful_registration(self, driver, fill_out_registration_form):
        user = NewUser()
        driver.get(REGISTRATION_PAGE_URL)
        fill_out_registration_form(driver, user.name, user.email, user.password)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(login_form_header))
        assert driver.find_element(*login_form_header).text == 'Вход'
        assert driver.current_url == LOGIN_PAGE_URL

    @pytest.mark.parametrize('password', ('p', 'passw'))
    def test_registration_with_short_password(self, driver, fill_out_registration_form, password):
        user = NewUser()
        driver.get(REGISTRATION_PAGE_URL)
        fill_out_registration_form(driver, user.name, user.email, password)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(wrong_password_error))
        assert driver.find_element(*wrong_password_error).text == 'Некорректный пароль'
        assert driver.current_url == REGISTRATION_PAGE_URL
