from locators import bun_button, filling_button, sauce_button
from urls import BASE_URL


class TestConstructor:
    def test_сonstructor_page_go_to_bun_section(self, driver):
        driver.get(BASE_URL)
        element = driver.find_element(*bun_button)
        assert '_current_' in element.get_dom_attribute('class')

    def test_сonstructor_page_go_to_sauce_section(self, driver):
        driver.get(BASE_URL)
        element = driver.find_element(*sauce_button)
        element.click()
        assert '_current_' in element.get_dom_attribute('class')

    def test_сonstructor_page_go_to_filling_section(self, driver):
        driver.get(BASE_URL)
        element = driver.find_element(*filling_button)
        element.click()
        assert '_current_' in element.get_dom_attribute('class')
