import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import RegisteredUser
from locators import (login_form_header, main_page_login_button,
                      main_page_order_create_button, personal_cabinet_button,
                      reg_page_login_button)
from urls import (BASE_URL, LOGIN_PAGE_URL, RECOVERY_PASSWORD_PAGE,
                  REGISTRATION_PAGE_URL)


@pytest.mark.parametrize('url, button',
                         ((BASE_URL, (By.XPATH, main_page_login_button,)),
                          (REGISTRATION_PAGE_URL, (By.CSS_SELECTOR, reg_page_login_button)),
                          (RECOVERY_PASSWORD_PAGE, (By.CSS_SELECTOR, reg_page_login_button)),
                          (BASE_URL, (By.CSS_SELECTOR, personal_cabinet_button))))
def test_successful_login_from_pages(driver, fill_out_auth_form, url, button):
    user = RegisteredUser()
    driver.get(url)
    driver.find_element(*button).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, login_form_header)))
    assert driver.current_url == LOGIN_PAGE_URL

    fill_out_auth_form(driver, user.email, user.password)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                      main_page_order_create_button)))
    assert driver.find_element(By.XPATH, main_page_order_create_button).is_displayed()
    assert driver.current_url == BASE_URL


