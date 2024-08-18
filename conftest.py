import ast

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import (form_button, form_email_input, form_name_input,
                      form_password_input, main_page_order_create_button)
from urls import BASE_URL, LOGIN_PAGE_URL


def pytest_addoption(parser):
    parser.addoption('--driver_type', default='chrome')
    parser.addoption('--headless', type=int, default=1)


@pytest.fixture
def driver_type(request):
    return request.config.getoption('--driver_type')


@pytest.fixture
def headless(request):
    return request.config.getoption('--headless')


@pytest.fixture(scope='function')
def driver(headless):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') if headless else None
    _driver = webdriver.Chrome(options=options)
    yield _driver
    _driver.quit()


@pytest.fixture
def fill_out_registration_form():
    def _fill_out_form(driver, name, email, password):
        driver.find_element(*form_name_input).send_keys(name)
        driver.find_element(*form_email_input).send_keys(email)
        driver.find_element(*form_password_input).send_keys(password)
        driver.find_element(*form_button).click()
    return _fill_out_form


@pytest.fixture
def fill_out_auth_form():
    def _fill_out_form(driver, email, password):
        driver.find_element(*form_email_input).send_keys(email)
        driver.find_element(*form_password_input).send_keys(password)
        driver.find_element(*form_button).click()
    return _fill_out_form


@pytest.fixture
def auth(fill_out_auth_form):
    def _auth(driver, email, password):
        driver.get(LOGIN_PAGE_URL)
        fill_out_auth_form(driver, email, password)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(main_page_order_create_button))
        assert driver.find_element(*main_page_order_create_button).is_displayed()
        assert driver.current_url == BASE_URL
    return _auth
