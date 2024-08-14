import pytest
from selenium.webdriver.common.by import By

from locators import bun_button, filling_button, sauce_button
from urls import BASE_URL


@pytest.mark.parametrize('section',
                         ((By.XPATH, bun_button),
                          (By.XPATH, sauce_button),
                          (By.XPATH, filling_button)))
def test_сonstructor_page_go_to_section(driver, section):
    driver.get(BASE_URL)
    element = driver.find_element(*section)
    if 'Булки' != element.text:
        element.click()
    assert '_current_' in element.get_dom_attribute('class')
